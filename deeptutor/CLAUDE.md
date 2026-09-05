# My-Deep-Proprietary Development Guide

This file provides Claude Code guidance for the **My-Deep-Proprietary** project — an extended deep learning setup with proprietary extensions and specialized agents.

---

## Foundation

### Core References

**Global Ecosystem** (84 agents, 66 skills)
- Location: /Users/steven/my-supremepowers/
- Use when: General development, architecture, utilities
- CLAUDE.md: /Users/steven/my-supremepowers/CLAUDE.md

**Deep Learning Hub** (18 agents, 9 skills)
- Location: /Users/steven/my-supremepowers/deep-learning/
- Symlinked: ./.claude/ → /Users/steven/my-supremepowers/deep-learning/
- Use when: Model training, optimization, evaluation, deployment
- CLAUDE.md: ./.claude/CLAUDE.md

### Principles

Inherit from:
1. **PRINCIPLES.md** — Context preservation through agent delegation
2. **RULES.md** — Mandatory enforcement rules
3. **deep-learning/CLAUDE.md** — DL-specific guidance

---

## Project-Specific Setup

### Purpose

**My-Deep-Proprietary** extends the DL hub with:
- Proprietary algorithms and extensions
- Custom agents for specialized tasks
- AVA-TAR overlay integration
- Advanced model architectures
- Production-grade deployment

### Structure

```
My-Deep-Proprietary/
├── deeptutor/              ← Core DL library + proprietary extensions
├── deeptutor_cli/          ← CLI with proprietary commands
├── deeptutor-mimic/        ← Proprietary enhancement module
├── AGENTS.md              ← Project agents + proprietary agents
├── CLAUDE.md              ← This file
├── AVA-TAR-OVERLAY.md     ← Proprietary integration documentation
├── .claude/ → symlink     ← Access to DL hub + global agents
└── ... other files
```

### Framework

- **Primary**: PyTorch (proprietary optimizations)
- **Secondary**: TensorFlow/Keras (benchmark comparisons)
- **Hugging Face**: For transformer extensions
- **Custom**: Proprietary optimizations and agents

---

## Getting Started

### Setup with Proprietary Extensions

```bash
cd /Users/steven/PYTHON_MARKETPLACE_MASTER/My-Deep-Proprietary
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Install proprietary extensions
pip install -e .
```

### Quick Development with Proprietary Tools

1. **Brainstorm** → Use `/brainstorming` skill (global)
2. **Design with proprietary agents** → Check AGENTS.md for custom agents
3. **Train with optimizations** → Use `/model-training-workflow` skill + proprietary tuning
4. **Advanced debugging** → Use `/pytorch-debugging` skill + proprietary tools
5. **Evaluate** → Use `/model-evaluation` skill + proprietary metrics
6. **Deploy** → Use `ml-ops-engineer` agent + proprietary infrastructure

---

## Project Agents

### Proprietary Agents (Local to This Project)

See **AGENTS.md** for:
- Custom optimization agents
- Proprietary training agents
- Advanced evaluation agents
- Specialized inference agents

### DL Hub Agents (18 Available)

All standard DL agents available via `./.claude/agents/`:
- neural-network-architect, pytorch-expert, tensorflow-expert
- huggingface-specialist, model-trainer
- dataset-optimizer, ml-ops-engineer, model-evaluator
- And 10 more...

### Global Agents (84 Available)

Access /Users/steven/my-supremepowers/agents/:
- backend-architect, code-reviewer, system-architect
- And 81 more for general development

---

## Advanced Features

### Proprietary Optimizations

Documented in **AVA-TAR-OVERLAY.md**:
- Custom training optimizations
- Proprietary architectures
- Specialized loss functions
- Advanced regularization strategies

### Custom Agents Integration

See **AGENTS.md** for:
- Which proprietary agents to spawn
- When to use proprietary vs standard DL agents
- Integration points with DL hub

### Model Registry

- Location: [Proprietary location]
- Versions: [Proprietary versioning scheme]
- Use agent: ml-ops-engineer (DL hub) + proprietary deployment

---

## Common Development Patterns

### Pattern 1: Proprietary Architecture Development

```
1. Design concept      → neural-network-architect agent
2. Implement custom    → Spawn proprietary architecture agent (see AGENTS.md)
3. Benchmark          → Compare against standard architectures
4. Train              → /model-training-workflow skill + proprietary tuning
5. Evaluate           → /model-evaluation skill + proprietary metrics
6. Optimize           → Apply proprietary optimizations
7. Deploy             → ml-ops-engineer agent + proprietary pipeline
```

### Pattern 2: Optimization & Tuning

```
1. Baseline model     → Train with standard approach
2. Profile           → Identify bottlenecks
3. Optimize          → Apply proprietary optimizations (see AVA-TAR-OVERLAY.md)
4. Validate          → Ensure correctness with /model-evaluation skill
5. Benchmark         → Compare improvement metrics
6. Document          → Update proprietary records
```

### Pattern 3: Research & Development

```
1. Literature review   → Use systematic-debugging skill (global)
2. Design algorithm    → neural-network-architect agent
3. Implement           → pytorch-expert agent + proprietary tools
4. Test               → /test-driven-development skill (global)
5. Benchmark          → /model-evaluation skill
6. Document           → Proprietary documentation
7. Publish internally → ml-ops-engineer for internal deployment
```

---

## Framework-Specific Guidance

### PyTorch with Proprietary Extensions

- **Expert**: pytorch-expert agent (DL hub) + proprietary extension agents
- **Skill**: /pytorch-debugging
- **Custom tools**: [See AVA-TAR-OVERLAY.md]
- **When**: All custom development uses proprietary PyTorch extensions

### TensorFlow Benchmarking

- **Expert**: tensorflow-expert agent
- **When**: Comparing against TensorFlow baselines
- **Note**: Secondary; use for validation only

### Hugging Face Transformer Extensions

- **Expert**: huggingface-specialist agent
- **Custom**: [Proprietary transformer extensions]
- **When**: NLP tasks with proprietary adaptations

---

## Testing & Validation

### Unit Testing
```bash
pytest tests/
pytest --cov=deeptutor tests/
```

### Proprietary Model Validation

See **AVA-TAR-OVERLAY.md** for:
- Proprietary validation metrics
- Comparison against baselines
- Performance requirements
- Quality gates

### Integration Testing

Use `/test-driven-development` skill + proprietary test suite

---

## Deployment

### Staging Deployment

Use `ml-ops-engineer` agent + proprietary staging pipeline to:
- Test in production-like environment
- Validate performance
- Check resource usage
- Verify monitoring

### Production Deployment

Use `deployment-pipeline-builder` agent + proprietary production pipeline:
- Automated validation gates
- Progressive rollout
- Monitoring and alerting
- Automatic rollback triggers

---

## Proprietary Integration

### AVA-TAR Overlay

See **AVA-TAR-OVERLAY.md** for:
- Integration with proprietary systems
- Custom optimization techniques
- Advanced features
- Internal deployment specifics

### Internal Communication

See **Communication.md** for:
- Team coordination
- Documentation standards
- Review processes
- Escalation procedures

---

## Troubleshooting

### Proprietary Agent Not Available?

1. Check **AGENTS.md** for agent name
2. Verify it's listed in proprietary agents section
3. If missing, create new agent (see AGENTS.md guidelines)

### Proprietary Optimization Not Working?

1. Check **AVA-TAR-OVERLAY.md** for setup instructions
2. Verify all dependencies installed
3. Run validation tests
4. Check proprietary error logs

### Performance Below Baseline?

1. Profile with PyTorch profiler
2. Compare against reference implementation
3. Use /pytorch-debugging skill
4. Consult AVA-TAR-OVERLAY.md documentation

---

## References

- **Project structure**: README.md
- **Contributing**: CONTRIBUTING.md
- **Proprietary details**: AVA-TAR-OVERLAY.md
- **Agents**: AGENTS.md
- **Communication**: Communication.md

---

## Integration with Other Projects

**Other PYTHON_MARKETPLACE_MASTER projects**:
- **mini_deep_setup** — Minimal setup, reference implementation
- **DeepTutor-main** — Full DeepTutor with curriculum
- **MY_DEEP_SETUP** — General specialization and courses

All share the same DL hub (/.claude symlink) and global ecosystem.

---

**Project**: My-Deep-Proprietary  
**Purpose**: Extended DL with proprietary extensions  
**Status**: ✓ Production ready  
**Last Updated**: 2026-05-11
