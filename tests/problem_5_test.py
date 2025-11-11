import pytest
from candidate_loader import get_candidates, AI_VARIANTS, FUNCTION_NAMES

PROBLEM_NUM = 5

# Each test case is (input_list, expected_output)
TEST_CASES = [
    ([1.0, 2.0, 3.0], 2.0/3.0),
    ([1.0, 2.0, 3.0, 4.0], 1.0),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 6.0/5.0),
]

variant_to_candidate = get_candidates(PROBLEM_NUM)
loaded_variants = [v for v in AI_VARIANTS if v in variant_to_candidate]

if not loaded_variants:
    pytest.skip(f"No valid variants loaded for problem {PROBLEM_NUM}", allow_module_level=True)


@pytest.mark.parametrize("variant", loaded_variants)
@pytest.mark.parametrize("input_args, expected", TEST_CASES)
def test_problem_variants(variant, input_args, expected):
    candidate = variant_to_candidate[variant]

    if isinstance(input_args, tuple):
        result = candidate(*input_args)
    else:
        result = candidate(input_args)

    if isinstance(result, float) and isinstance(expected, float):
        assert abs(result - expected) < 1e-6
    else:
        assert result == expected