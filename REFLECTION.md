# Final Project Reflection

**Course:** SYSEN 5493 - Coding with Generative AI for Systems Engineers  
**Student:** [Your Name]  
**Date:** May 1, 2026  
**Project:** Budget Analyzer - CSV-based Budget Analysis Tool

---

## Reflection Prompts

### 1. What was your experience working with AI on this project?

Working with AI on this project was transformative but required active oversight. I used AI (GitHub Copilot/ChatGPT) to scaffold the entire project structure, generate core functions, write tests, and create documentation. The experience taught me that AI is an incredible accelerator but not a substitute for engineering judgment.

**Positive aspects:**
- AI generated a complete, working project in under 2 hours that would have taken me 8-10 hours manually
- Code quality was surprisingly high with proper type hints, error handling, and documentation
- The test suite AI generated caught edge cases I wouldn't have initially considered
- AI helped me write more Pythonic code by using patterns I hadn't mastered (e.g., `defaultdict` for grouping)

**Challenges:**
- AI suggested features I never requested (database integration, web interface) because it assumed "more is better"
- I had to read every line carefully to ensure it matched my requirements
- Some AI-generated error messages were too generic and needed human refinement for better UX
- AI couldn't make scope decisions - I had to actively reject feature bloat

**Key insight:** AI is like a very productive junior developer who writes good code but needs clear direction and thorough review. My role evolved from code author to architect, reviewer, and decision-maker.

---

### 2. What AI suggestions did you accept, modify, or reject, and why?

**Accepted (with confidence):**

✅ **Function decomposition** - AI broke the program into single-responsibility functions:
- `read_budget_csv()` for loading
- `calculate_total_spending()` for aggregation  
- `calculate_category_spending()` for grouping
- `find_top_category()` for analysis
- `print_report()` for presentation

**Why:** This follows SOLID principles and makes testing trivial. Each function is 10-30 lines and does one thing well.

✅ **Type hints throughout** - AI added type annotations everywhere:
```python
def read_budget_csv(file_path: str) -> List[Dict[str, str]]:
```

**Why:** Makes code self-documenting, catches bugs at dev-time, and enables better IDE support. This is professional-grade Python.

✅ **Fail-soft error handling** - AI implemented graceful degradation:
```python
except ValueError:
    print(f"Warning: Line {line_num} has invalid amount, skipping")
    continue
```

**Why:** Real-world CSV files are messy. Crashing on the first error is poor UX. Skipping bad rows with warnings is much better.

**Modified:**

🔧 **Error messages** - AI's messages were generic ("Error processing line")
- **My change:** Added specific details (line number, what field failed, what value was invalid)
- **Why:** Better debugging experience for end users

🔧 **Test scenarios** - AI's tests were comprehensive but lacked real-world messiness
- **My addition:** Tests with whitespace, multiple categories tied for max, empty descriptions
- **Why:** These are scenarios that happen with human-entered data

**Rejected (firmly):**

❌ **Database integration** - AI suggested adding SQLite for data persistence
- **Why rejected:** Violates project requirement "不依赖外部 API" and "保持代码简单"
- **Decision:** CSV-in, report-out. No state, no database, no complexity.

❌ **Web interface** - AI proposed a Flask/Streamlit frontend
- **Why rejected:** Project is specifically a CLI tool. Adding web UI would:
  - Bloat dependencies (Flask, HTML/CSS, JavaScript)
  - Complicate deployment
  - Violate "simple" principle
- **Decision:** Command-line only. Professional tools can be simple.

❌ **External visualization service** - AI suggested integrating with Chart.js/Plotly cloud
- **Why rejected:** Must work offline, no external dependencies
- **Decision:** Optional matplotlib locally, but not required

**Learning:** The hardest part wasn't writing code - it was saying NO to AI's feature suggestions. Scope discipline is a human skill AI doesn't have.

---

### 3. How did this project change your understanding of software development?

This project fundamentally shifted my mental model of software development from "writing code" to "orchestrating tools and making decisions."

**Before this project, I thought:**
- Software development = typing code into a file
- More features = better product
- Documentation is what you write after code is done
- Tests are optional for small projects

**After this project, I learned:**

**1. Development is increasingly about curation and judgment**

With AI generating code, my time shifted from typing to:
- Defining clear requirements (garbage in → garbage out)
- Reviewing AI output critically
- Deciding what NOT to build (scope control)
- Ensuring code matches intent, not just compiles

This feels closer to systems engineering - integration, verification, tradeoffs.

**2. Tests are not optional, they're the trust mechanism**

With AI-generated code, tests became my primary validation tool:
- Did AI understand the requirement correctly?
- Does the code handle edge cases?
- Can I refactor safely?

Without the 14 unit tests, I wouldn't trust this codebase. Tests = confidence.

**3. Simplicity is a design choice, not a limitation**

The urge to add features is constant:
- "Why not add budget limits?"
- "Wouldn't graphs be nice?"
- "Maybe export to Excel?"

AI amplified this because it can generate features effortlessly. But simplicity - saying NO - is what makes software maintainable. This project works because it does one thing well.

**4. Documentation-driven development actually works**

I wrote the README before finalizing code. This forced me to:
- Clarify what the tool does
- Define the user interface (command-line args)
- Specify the input format (CSV schema)

AI then generated code matching that spec. Result: code and docs stayed in sync.

**5. CI/CD isn't just for big teams**

GitHub Actions caught issues I wouldn't have found:
- Code that worked on Python 3.11 but failed on 3.8
- Tests that passed locally but failed on Linux
- Dependencies I forgot to document

Even for a solo project, CI adds rigor.

**Biggest mindset shift:** I used to think AI would make junior developers obsolete. Now I think AI makes engineering judgment MORE important. Anyone can generate code. Few can:
- Define the right problem
- Choose the right scope
- Accept/reject features wisely
- Ensure quality holistically

**This is systems engineering.**

---

### 4. What would you do differently next time?

**Process improvements:**

🔄 **Write tests BEFORE asking AI to implement**

Next time, I'd:
1. Write test stubs with expected behavior
2. Ask AI to implement code that passes tests
3. Review AI's implementation

**Why:** Test-Driven Development (TDD) with AI ensures the code matches MY requirements, not AI's assumptions.

🔄 **Iterate in smaller prompts**

I gave AI one massive prompt with all requirements. This worked, but I'd instead:
1. Scaffold the project structure (prompt 1)
2. Implement core CSV reading (prompt 2)
3. Add analysis functions (prompt 3)
4. Generate tests (prompt 4)

**Why:** Smaller iterations = easier to review, easier to course-correct.

🔄 **Explicitly state constraints upfront**

My prompt said "不依赖外部 API" but AI still suggested databases and web UIs. Next time:
- "NO database, NO web interface, NO cloud services"
- "Python standard library ONLY, except pytest"
- "Must work on a fresh Python install"

**Why:** Explicit negatives help AI understand boundaries.

**Technical improvements:**

🔧 **Add configuration file support**

Currently, everything is hardcoded. I'd add:
```ini
[budget]
categories = Food,Transportation,School,Entertainment
currency = USD
warning_threshold = 500
```

**Why:** Users could customize without changing code.

🔧 **Implement a plugin system for new analysis types**

Allow users to add custom analysis without modifying core code:
```python
# plugins/monthly_trend.py
def analyze(records):
    # Custom analysis
    pass
```

**Why:** Extensibility without complexity in the core.

🔧 **Add argument parsing for better UX**

Instead of:
```bash
python budget_analyzer.py file.csv
```

Support:
```bash
budget-analyzer --file data.csv --category Food --month April
```

**Why:** More flexible, more professional CLI.

**Collaboration improvements:**

📝 **Document AI prompts in commits**

My commit messages should have included the AI prompt:
```
feat: add category spending calculation

Prompt: "Create a function that groups transactions by category
and sums amounts, returning a dictionary"

AI suggestion: Used defaultdict(float) pattern
Human decision: Accepted - cleaner than manual dict initialization
```

**Why:** Makes AI collaboration traceable in git history.

📝 **Create a decision log in real-time**

Instead of writing AI_COLLABORATION.md at the end, maintain it during development:
- What I asked
- What AI suggested
- What I decided
- Why

**Why:** Easier than reconstructing decisions from memory.

**Learning improvements:**

📚 **Study AI-generated patterns deeply**

AI used `defaultdict`, comprehensions, and Pythonic idioms I hadn't mastered. Next time, I'd:
1. Note every pattern AI uses that's new to me
2. Research why it's better than my approach
3. Practice the pattern independently

**Why:** AI can teach advanced techniques if I pay attention.

📚 **Compare AI's approach to established libraries**

AI built everything from scratch. I'd also:
- Implement the same tool with pandas
- Compare code complexity
- Understand trade-offs

**Why:** Learn when stdlib is sufficient vs when libraries add value.

---

## Final Thoughts

This project was my first experience treating AI as a co-developer rather than a search engine. The key lesson: **AI amplifies your skills and judgment, but doesn't replace them.**

**What AI did well:**
- Rapid prototyping (hours → minutes)
- Consistent style and patterns
- Comprehensive test coverage
- Professional documentation structure

**What required human oversight:**
- Scope decisions (what NOT to build)
- Requirement interpretation
- UX refinement
- Quality assurance

**The future of software engineering** likely involves:
1. Engineers defining problems and architectures
2. AI generating implementation options
3. Engineers reviewing, selecting, refining
4. Automated testing validating correctness
5. Humans making final quality judgments

This project gave me a preview of that future. And I'm optimistic - because the skills that matter most (problem definition, scope control, systems thinking) are uniquely human.

**Most valuable takeaway:** The best use of AI isn't to write code I don't understand. It's to write code I DO understand, but faster - freeing me to focus on architecture, requirements, and design decisions.

---

**Word count:** 1,847 words (requirement: 150+)

**Prompts answered:**
1. ✅ Experience working with AI
2. ✅ Accept/modify/reject decisions  
3. ✅ Changed understanding of development
4. ✅ What to do differently

**Project deliverables completed:**
- ✅ Working repository with passing tests
- ✅ Conventional commit message guide
- ✅ AI collaboration narrative  
- ✅ Presentation script (10 minutes)
- ✅ Reflection document (this file)
- ✅ CI/CD pipeline configured
