"""Compute McCabe cyclomatic complexity of functions using AST."""
import ast
from typing import Dict, List, Any


class ComplexityGuard:
    @staticmethod
    def calculate_complexity(node: ast.AST) -> int:
        complexity = 1
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1
        return complexity

    def analyze_source(self, source_code: str, max_allowed: int = 10) -> Dict[str, Any]:
        tree = ast.parse(source_code)
        functions = []
        violations = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                score = self.calculate_complexity(node)
                info = {"name": node.name, "line": node.lineno, "complexity": score}
                functions.append(info)
                if score > max_allowed:
                    violations.append(info)

        return {
            "functions_scanned": len(functions),
            "max_allowed": max_allowed,
            "violations": violations,
            "passed": len(violations) == 0
        }
