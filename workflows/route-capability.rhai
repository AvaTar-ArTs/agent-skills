let meta = #{
    name: "route-capability",
    description: "Locate one capability under ~/.agent-skills and contrast canonical paths with copies",
    when_to_use: "A slash command or skill name may have loaded the wrong host copy",
    phases: [
        #{ title: "Locate", detail: "canonical tree only" },
        #{ title: "Contrast", detail: "which path to use" },
    ],
};

let locate_schema = #{
    "type": "object",
    "required": ["canonical", "copies", "notes"],
    "properties": #{
        "canonical": #{ "type": "array", "maxItems": 8, "items": #{ "type": "string" } },
        "copies": #{ "type": "array", "maxItems": 8, "items": #{ "type": "string" } },
        "notes": #{ "type": "string" },
    },
};

let contrast_schema = #{
    "type": "object",
    "required": ["route", "skip", "reason"],
    "properties": #{
        "route": #{ "type": "array", "maxItems": 6, "items": #{ "type": "string" } },
        "skip": #{ "type": "array", "maxItems": 8, "items": #{ "type": "string" } },
        "reason": #{ "type": "string" },
    },
};

let cap = if args == () { () } else { args.name };
if cap == () {
    pause("verification", "Pass args.name — the skill or agent to route.");
}

phase("Locate");
let prompt = "Locate capability '";
prompt += cap;
prompt += "' only under /Users/steven/.agent-skills. Use eza, rg, and fzf. Do not scan the rest of the home directory and do not follow symlinks outside that tree. Return canonical paths (skills/ and agents/ source files) and copies (iterm2, marketplace, .tmp, host mirrors). Empty lists are valid only after you have searched.";
let loc = agent(prompt, #{
    label: "locate",
    capability_mode: "read-only",
    output_schema: locate_schema,
});

if loc == () || loc.success != true || loc.output == () {
    complete(#{ summary: "Locate did not return evidence.", route: [], skip: [] });
}

phase("Contrast");
let body = "Classify these paths for capability '";
body += cap;
body += "'. Canonical wins. Skip marketplace, .tmp, backups, and host copies that disagree on paths. Prefer sage and agent-workflow-catalog before create-hook or v3 CLI work. Evidence:\n";
body += json_encode(loc.output);
let verdict = agent(body, #{
    label: "contrast",
    capability_mode: "read-only",
    output_schema: contrast_schema,
});

if verdict == () || verdict.success != true || verdict.output == () {
    complete(#{ summary: "Contrast did not return evidence.", route: [], skip: [] });
}

let report = "# Route\n\n";
report += cap;
report += "\n\n";
report += verdict.output.reason;
let path = write_scratch_file("route.md", report);
log("route written");
complete(#{ summary: "Routed " + cap, path: path, route: verdict.output.route, skip: verdict.output.skip });
