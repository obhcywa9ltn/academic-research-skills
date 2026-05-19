"""
academic-research-skills: A toolkit for developing and assessing academic research competencies.

This package provides tools for:
- Evaluating research question formulation
- Assessing literature review quality
- Checking citation and reference formatting
- Analyzing argument structure and logical coherence
- Providing feedback on research methodology
"""

__version__ = "0.1.0"
__author__ = "academic-research-skills contributors"
__license__ = "MIT"

from academic_research_skills.core.evaluator import ResearchSkillsEvaluator
from academic_research_skills.core.feedback import FeedbackGenerator
from academic_research_skills.core.rubric import ResearchRubric

__all__ = [
    "ResearchSkillsEvaluator",
    "FeedbackGenerator",
    "ResearchRubric",
    "__version__",
]
