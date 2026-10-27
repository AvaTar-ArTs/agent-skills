let meta = #{
    name: "deduce-goal",
    description: "Deduce one matching skill or flow from a user goal",
    when_to_use: "Need to classify a request against existing use cases and invoke one flow",
    phases: [
        #{ title: "Deduce", detail: "one classifier against live indexes" },
    ],
};

let deduce_schema = #{
    "type": "object",
    "required": ["use_case", "skill", "flow", "reason"],
    "properties": #{
        "use_case": #{ "type": "string" },
        "skill": #{ "type": "string" },
        "flow": #{ "type": "string" },
        "reason": #{ "type": "string" },
    },
};

let goal = if args == () { () } else { args.goal };
if goal == () {
    pause("verification", "Pass args.goal — the user request to classify.");
}

phase("Deduce");
let prompt = "Deduce exactly one matching skill or flow for this user goal. Read /Users/steven/.cursor/docs/USE_CASES_AND_TRIGGERS.md then /Users/steven/.qwen/Logic_Flows.md with read_file. Prefer canonical paths under /Users/steven/.agent-skills. Do not inventory copies. Do not scan home. Do not follow symlinks out of those trees. Goal:\n";
prompt += json_encode(goal);
prompt += "\nReturn use_case (section title from the trigger index), skill (one canonical SKILL.md or agent path), flow (one documented sequence), reason (one sentence). If nothing matches, set skill to /Users/steven/.agent-skills/skills/using-superpowers/SKILL.md and flow to classify-again.";

let r = agent(prompt, #{
    label: "deduce",
    capability_mode: "read-only",
    output_schema: deduce_schema,
});

if r == () || r.success != true || r.output == () {
    complete(#{ summary: "Deduce did not return evidence.", use_case: "", skill: "", flow: "" });
}

let report = "# Deduce\n\n";
report += r.output.use_case;
report += "\n";
report += r.output.skill;
report += "\n";
report += r.output.flow;
report += "\n";
report += r.output.reason;
let path = write_scratch_file("deduce.md", report);
log("deduced");
complete(#{
    summary: r.output.skill,
    path: path,
    use_case: r.output.use_case,
    skill: r.output.skill,
    flow: r.output.flow,
    reason: r.output.reason,
});
