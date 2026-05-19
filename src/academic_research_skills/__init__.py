"""academic-research-skills: A toolkit for developing and assessing academic research competencies.

This package provides tools for:
- Evaluating research question formulation
- Assessing literature review quality
- Checking citation and reference formatting
- Analyzing argument structure and logical coherence
- Providing feedback on research methodology

Personal fork notes:
- Using this package to help evaluate undergraduate thesis drafts
- See examples/ directory for sample rubrics tailored to social science research
- Added DEFAULT_CITATION_STYLE = "APA" since all my students use APA 7th edition
"""

__version__ = "0.1.0"
__author__ = "academic-research-skills contributors"
__license__ = "MIT"

# Default citation style for my undergraduate social science courses (APA 7th edition)
DEFAULT_CITATION_STYLE = "APA"

from academic_research_skills.core.evaluator import ResearchSkillsEvaluator
from academic_research_skills.core.feedback import FeedbackGenerator
from academic_research_skills.core.rubric import ResearchRubric

__all__ = [
    "ResearchSkillsEvaluator",
    "FeedbackGenerator",
    "ResearchRubric",
    "DEFAULT_CITATION_STYLE",
    "__version__",
]
