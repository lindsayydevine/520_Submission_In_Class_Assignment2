from importlib import import_module

# List all AI solution types
AI_VARIANTS = [
    "LLaMa_Chain_As_Thought",
    "LLaMa_Self_Debugging",
    "Vicuna_Chain_As_Thought",
    "Vicuna_Self_Debugging"
]

# Map problem number to the main function name for that problem
FUNCTION_NAMES = {
    1: "has_close_elements",
    2: "separate_paren_groups",
    3: "truncate_number",
    4: "below_zero",
    5: "mean_absolute_deviation",
    6: "intersperse",
    7: "parse_nested_parens",
    8: "filter_by_substring",
    9: "sum_product",
    10: "rolling_max"
}

def get_candidates(problem_number):
    func_name = FUNCTION_NAMES[problem_number]
    variant_to_candidate = {}

    for variant in AI_VARIANTS:
        module_path = f"generated_code_solutions_with_candidate.problem_{problem_number}.{variant}_Problem{problem_number}"
        try:
            module = import_module(module_path)

            if hasattr(module, func_name):
                candidate_func = getattr(module, func_name)
            elif hasattr(module, "candidate"):
                candidate_func = getattr(module, "candidate")
            else:
                continue

            if not callable(candidate_func):
                print(f"[Warning] {module_path}.{func_name} is not callable, skipping")
                continue

            variant_to_candidate[variant] = candidate_func

        except Exception as e:
            print(f"[Warning] Failed to load {module_path}: {type(e).__name__}: {e}")

    return variant_to_candidate

