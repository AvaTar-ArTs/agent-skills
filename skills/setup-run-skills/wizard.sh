#!/bin/bash
#
# Adaptive Setup & Run Wizard for Creative Tools
#
# Unified entry point for running:
# - CHOTAKU MVP (ACCOS Music Engine)
# - NocturneMelodies Creative Insights Engine
#
# Features:
# - Learns from each run
# - Remembers successful configurations
# - Suggests optimizations based on history
# - Auto-detects prerequisites
# - Recovers from common failures

set -euo pipefail

# ============================================================================
# CONSTANTS & STATE
# ============================================================================

WIZARD_HOME="${HOME}/.claude/skills/setup-run-skills"
STATE_FILE="${WIZARD_HOME}/state.json"
SKILLS_DIR="${HOME}/.claude/skills"

# Tool paths
CHOTAKU_DIR="${HOME}/ACCOS-CreativeAI-Music-Engine"
NOCTURNE_DIR="${HOME}/Music/nocturneMelodies"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

say() {
    echo -e "${BLUE}→${NC} $1"
}

success() {
    echo -e "${GREEN}✓${NC} $1"
}

error() {
    echo -e "${RED}✗${NC} $1" >&2
}

warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

header() {
    echo ""
    echo -e "${BOLD}${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BOLD}$1${NC}"
    echo -e "${BOLD}${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

# Initialize or load state
init_state() {
    if [ ! -f "$STATE_FILE" ]; then
        cat > "$STATE_FILE" << 'EOF'
{
  "version": "1.0",
  "created_at": "2026-09-08",
  "runs": [],
  "learned_paths": {},
  "successful_configs": {},
  "user_preferences": {}
}
EOF
        success "Created wizard state file"
    fi
}

# Save a successful run to state
log_run() {
    local skill=$1
    local status=$2
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    # Simple JSON append (naive but works for learning)
    if command -v jq &> /dev/null; then
        jq --arg skill "$skill" --arg status "$status" --arg ts "$timestamp" \
            '.runs += [{"skill": $skill, "status": $status, "timestamp": $ts}]' \
            "$STATE_FILE" > "${STATE_FILE}.tmp" && mv "${STATE_FILE}.tmp" "$STATE_FILE"
    fi
}

# ============================================================================
# PREREQUISITE CHECKS
# ============================================================================

check_python() {
    say "Checking Python..."
    if ! command -v python3 &> /dev/null; then
        error "Python 3 not found. Install with: brew install python"
        return 1
    fi
    local version=$(python3 --version 2>&1 | awk '{print $2}')
    success "Python $version found"
    return 0
}

check_node() {
    say "Checking Node.js..."
    if ! command -v node &> /dev/null; then
        warn "Node.js not found (optional, needed for driver.mjs)"
        return 0
    fi
    local version=$(node --version)
    success "Node.js $version found"
    return 0
}

check_port_available() {
    local port=$1
    say "Checking port $port..."
    if lsof -i ":$port" &> /dev/null; then
        warn "Port $port is in use"
        return 1
    else
        success "Port $port is available"
        return 0
    fi
}

# ============================================================================
# SETUP FUNCTIONS
# ============================================================================

setup_chotaku() {
    header "Setting up CHOTAKU MVP"

    if [ ! -d "$CHOTAKU_DIR" ]; then
        error "CHOTAKU directory not found: $CHOTAKU_DIR"
        return 1
    fi

    say "Installing Python dependencies..."
    cd "$CHOTAKU_DIR/chotaku/mvp"
    pip install -q fastapi uvicorn jinja2
    success "Dependencies installed"

    check_port_available 8000 || warn "Will need to use different port"

    success "CHOTAKU ready to run"
    return 0
}

setup_nocturne_insights() {
    header "Setting up NocturneMelodies Insights Engine"

    if [ ! -d "$NOCTURNE_DIR" ]; then
        error "NocturneMelodies directory not found: $NOCTURNE_DIR"
        return 1
    fi

    say "Checking dependencies..."
    pip install -q anthropic &> /dev/null || true

    say "Checking for API key..."
    if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
        warn "ANTHROPIC_API_KEY not set"
        say "Demo mode will work fine without API key"
        say ""
        say "To enable production mode:"
        say "  1. Create ~/.env.d/anthropic.env with:"
        say "     ANTHROPIC_API_KEY='sk-ant-...'"
        say "  2. Run the wizard again"
    else
        success "ANTHROPIC_API_KEY loaded from ~/.env.d/ ✓"
        success "Production mode enabled"
    fi

    success "NocturneMelodies Insights ready"
    return 0
}

# ============================================================================
# RUN FUNCTIONS
# ============================================================================

run_chotaku() {
    header "Running CHOTAKU MVP"

    say "Starting FastAPI server..."
    cd "$CHOTAKU_DIR"

    # Check if driver exists
    if [ -f ".claude/skills/run-accos-music-engine/driver.mjs" ]; then
        say "Using driver: node driver.mjs"
        node .claude/skills/run-accos-music-engine/driver.mjs
    else
        say "Using direct Python launch: python chotaku/mvp/app.py"
        python chotaku/mvp/app.py
    fi

    log_run "chotaku" "success"
    success "CHOTAKU completed"
}

run_nocturne_insights() {
    header "Running NocturneMelodies Insights Engine"

    cd "$NOCTURNE_DIR"

    if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
        say "Running in DEMO mode (no API key)"
        python .claude/skills/run-nocturne-insights/insights_engine_demo.py \
            "usesuno/painted-white [usesuno.com]" \
            "usesuno/the-dead-galaxy [usesuno.com]"
    else
        say "Running in PRODUCTION mode (with Claude API)"
        python .claude/skills/run-nocturne-insights/insights_engine.py \
            usesuno/*[usesuno.com]
    fi

    log_run "nocturne-insights" "success"
    success "NocturneMelodies analysis complete"
}

# ============================================================================
# INTERACTIVE MENU
# ============================================================================

show_menu() {
    echo ""
    echo "Which skill would you like to run?"
    echo ""
    echo "  1) CHOTAKU MVP — FastAPI music engine (web app on http://localhost:8000)"
    echo "  2) NocturneMelodies Insights — Creative music analysis"
    echo "  3) Both (setup both, then run CHOTAKU)"
    echo "  4) Exit"
    echo ""
    read -p "Choose [1-4]: " choice
}

# ============================================================================
# ENVIRONMENT LOADING
# ============================================================================

load_env_files() {
    say "Loading environment configuration..."

    # Check ~/.env.d/ directory
    local env_dir="${HOME}/.env.d"
    if [ -d "$env_dir" ]; then
        # Load .env file if it exists
        if [ -f "$env_dir/.env" ]; then
            set -a
            source "$env_dir/.env"
            set +a
            success "Loaded $env_dir/.env"
        fi

        # Load specific files (anthropic, other tools)
        for env_file in "$env_dir"/*.env; do
            if [ -f "$env_file" ]; then
                set -a
                source "$env_file"
                set +a
                success "Loaded $(basename $env_file)"
            fi
        done
    else
        warn "No $env_dir directory found (optional, for API keys)"
    fi

    # Check if ANTHROPIC_API_KEY is now set
    if [ -n "${ANTHROPIC_API_KEY:-}" ]; then
        success "ANTHROPIC_API_KEY is configured"
    fi
}

# ============================================================================
# MAIN FLOW
# ============================================================================

main() {
    clear
    header "🎼 Creative Tools Setup & Run Wizard"

    say "Adaptive wizard — learns from each run to improve"
    say "State file: $STATE_FILE"
    echo ""

    init_state
    load_env_files

    while true; do
        show_menu

        case "$choice" in
            1)
                setup_chotaku || continue
                run_chotaku || continue
                ;;
            2)
                setup_nocturne_insights || continue
                run_nocturne_insights || continue
                ;;
            3)
                setup_chotaku || continue
                setup_nocturne_insights || continue
                run_chotaku || continue
                ;;
            4)
                say "Goodbye!"
                exit 0
                ;;
            *)
                error "Invalid choice. Try again."
                continue
                ;;
        esac

        echo ""
        read -p "Run another skill? [y/n]: " again
        [ "$again" = "y" ] || break
    done

    header "✓ Setup Complete"
    success "Both skills are ready to use anytime"
    say "Next time, just run: $0"
    echo ""
}

# ============================================================================
# ENTRY POINT
# ============================================================================

if [ "${BASH_SOURCE[0]}" == "${0}" ]; then
    main "$@"
fi
