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
- Added DEFAULT_FEEDBACK_VERBOSITY = "detailed" so students get thorough explanations
- Set DEFAULT_MAX_FEEDBACK_ITEMS = 5 to avoid overwhelming students with too many notes at once
- Increased DEFAULT_MAX_FEEDBACK_ITEMS to 7 for senior thesis students who need more granular feedback
- Added DEFAULT_LANGUAGE = "en" for explicit language tagging in feedback output
"""

__version__ = "0.1.0"
__author__ = "academic-research-skills contributors"
__license__ = "MIT"

# Default citation style for my undergraduate social science courses (APA 7th edition)
DEFAULT_CITATION_STYLE = "APA"

# Undergrads benefit from detailed feedback rather than terse summaries
DEFAULT_FEEDBACK_VERBOSITY = "detailed"

# Raised from 5 to 7 — senior thesis students can handle more feedback points per section
# and their drafts tend to have more nuanced issues worth flagging individually
DEFAULT_MAX_FEEDBACK_ITEMS = 7

# Explicitly set language to English; useful if multilingual support is added later
DEFAULT_LANGUAGE = "en"

from academic_research_skills.core.evaluator import ResearchSkillsEvaluator
from academic_research_skills.core.feedback import FeedbackGenerator
from academic_research_skills.core.rubric import ResearchRubric

__all__ = [
    "ResearchSkillsEvaluator",
    "FeedbackGenerator",
    "ResearchRubric",
    "DEFAULT_CITATION_STYLE",
    "DEFAULT_FEEDBACK_VERBOSITY",
    "DEFAULT_MAX_FEEDBACK_ITEMS",
    "DEFAULT_LANGUAGE",
    "__version__",
]
