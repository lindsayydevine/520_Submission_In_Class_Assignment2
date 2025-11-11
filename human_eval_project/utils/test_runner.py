import importlib.util
from pathlib import Path
import pytest
import sys
import types

def load_candidate(solution_file: Path, function_name="candidate"):
    """Dynamically load a solution file and return the candidate function."""
    spec = importlib.util.spec_from_file_location(solution_file.stem, solution_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # executes the whole file including imports
    return getattr(module, function_name)

def run_test_file_with_candidate(test_file: Path, candidate_func):
    """Run a pytest test file with a dynamically injected candidate function."""
    test_module_name = "dynamic_test_module"
    module = types.ModuleType(test_module_name)
    module.candidate = candidate_func
    sys.modules[test_module_name] = module
    pytest.main([str(test_file), f"--override-namespace=candidate={candidate_func}"])
