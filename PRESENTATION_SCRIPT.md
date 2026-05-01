# Budget Analyzer - 10 Minute Presentation Script

**Total Time: 10 minutes**
**Format: Live or Recorded**

---

## Slide 1: Title & Hook (0:00 - 1:00)

### Visual
- Title: "Budget Analyzer: A Simple CLI Tool for Personal Finance"
- Subtitle: "Built with AI Collaboration for SYSEN 5493"
- Your name and date

### Script

> "Hi everyone. I'm going to present Budget Analyzer, a command-line tool I built for analyzing personal spending data.
>
> **Here's the problem:** Most of us track our expenses in spreadsheets, but manually calculating totals, finding spending patterns, and identifying where our money goes is tedious and error-prone.
>
> **My solution:** A Python CLI tool that reads a simple CSV file and instantly tells you:
> - Where you spent the most money
> - How much you spent in each category
> - Your average transaction amount
> - All with automatic error handling for messy data
>
> **Why this matters:** It's simple, portable, works offline, and requires zero setup beyond Python. No databases, no cloud services, no complexity.
>
> Let me show you how it works."

**[TRANSITION]** → Move to architecture slide

---

## Slide 2: Project Structure (1:00 - 2:30)

### Visual
```
budget-analyzer/
├── src/budget_analyzer.py    ← Core logic
├── tests/test_budget_analyzer.py  ← 14 unit tests
├── data/sample_budget.csv    ← Example data
├── .github/workflows/ci.yml  ← Automated testing
└── README.md
```

### Script

> "The project follows a clean structure:
>
> **Core code** is in `budget_analyzer.py` - about 300 lines with type hints and comprehensive error handling.
>
> **Testing** uses pytest with 14 unit tests covering:
> - Normal operation
> - Invalid data handling
> - Edge cases like empty files and malformed amounts
>
> **CI/CD** runs automatically on GitHub Actions, testing against Python 3.8 through 3.11.
>
> **Design philosophy:** Keep it simple. No external dependencies except pytest. Everything runs locally. The CSV format is the 'API' - that's it.
>
> **Why this architecture?** 
> - Each function has one job (Single Responsibility)
> - Type hints catch errors early
> - Tests give me confidence to refactor
> - CI ensures it works everywhere, not just my machine"

**[TRANSITION]** → "Now let me show you this in action"

---

## Slide 3: Live Demo (2:30 - 5:30)

### Preparation
- Have terminal open in project directory
- Sample CSV file ready
- Backup video queued (in case of failure)

### Demo Script

> "Let me demonstrate with real data. Here's a CSV file with 15 spending transactions:"

**[SHOW CSV FILE]**
```bash
cat data/sample_budget.csv
```

> "As you can see - dates, categories, descriptions, and amounts. Simple format anyone can create in Excel."

**[RUN THE ANALYZER]**
```bash
python src/budget_analyzer.py data/sample_budget.csv
```

**[WAIT FOR OUTPUT]**

> "And here's what we get:
>
> Total spending: $307.89 across 15 transactions
>
> Category breakdown:
> - Food: $131 (43% of spending) 
> - Entertainment: $69
> - Transportation: $56
> - School: $50
>
> Top category: Food at $131
>
> Average transaction: About $20
>
> The report is clear, formatted, and immediately actionable."

**[SHOW ERROR HANDLING]**

> "Now let me show you something important - error handling."

**[CREATE BAD CSV OR SHOW EXISTING]**
```bash
# Show a CSV with invalid amount
echo "2026-05-01,Food,Lunch,not_a_number" >> bad_data.csv
python src/budget_analyzer.py bad_data.csv
```

> "Notice: it warns about the bad line but keeps processing. In the real world, data is messy - this tool doesn't crash, it adapts."

**[RUN TESTS]**
```bash
pytest -v
```

> "All 14 tests pass. These cover:
> - Valid data scenarios
> - Invalid amounts
> - Missing files
> - Empty data
> - Whitespace handling
>
> This gives me confidence the code works."

**[TRANSITION]** → "Now let me talk about how AI helped build this"

---

## Slide 4: AI Collaboration (5:30 - 7:00)

### Visual
- Screenshot of your initial prompt (in Chinese)
- Side-by-side comparison: "AI Suggested" vs "I Decided"

### Script

> "This project was built with substantial AI assistance, but I made all final decisions.
>
> **My initial prompt** was very specific - I gave AI:
> - Exact CSV format
> - Required output format
> - Testing requirements
> - CI/CD needs
>
> **What AI generated:**
> - Complete project scaffold (~2 hours of work in minutes)
> - Core functions with type hints
> - Comprehensive test suite
> - GitHub Actions config
> - Documentation templates
>
> **What I accepted:**
> - Function decomposition - clean single-responsibility design
> - Error handling pattern - fail-soft approach
> - Test coverage strategy - comprehensive edge cases
> - Type hints - makes code more maintainable
>
> **What I rejected:**
> - Database integration - AI suggested SQLite
>    - **Why rejected:** Violates 'keep it simple' requirement
>    - Added unnecessary complexity
>
> ❌ Web interface - AI proposed Flask frontend  
>    - **Why rejected:** Project is CLI-only
>    - Would bloat dependencies
>
> - External API integration
>    - **Why rejected:** Must work offline
>
> **Critical insight:** AI is excellent at generating code, but I had to be the gatekeeper. Every AI suggestion was reviewed, tested, and either accepted, modified, or rejected based on project goals.
>
> **Example modification:** AI's error messages were generic. I enhanced them to show line numbers and specific problems - much better UX."

**[TRANSITION]** → "So what surprised me?"

---

## Slide 5: What Surprised Me (7:00 - 8:30)

### Visual
- Bullet points of key learnings

### Script

> "Three things surprised me during this project:
>
> **1. AI's strengths and weaknesses became very clear**
>
> - **Strong at:** Boilerplate, test scaffolds, documentation templates
> - **Weak at:** Understanding implicit constraints, scope decisions
> - **Example:** AI suggested features I never asked for because it assumed 'more is better'
>
> **2. The importance of specificity in prompts**
>
> - My first prompt was 500+ words with exact requirements
> - **Result:** AI's output was 90% usable
> - **Learning:** Garbage in, garbage out. Clear requirements = good code.
>
> **3. I learned better Python from reviewing AI code**
>
> - AI used `defaultdict` for category grouping - elegant pattern I hadn't considered
> - Type hints throughout made me write more professional code
> - Testing patterns showed me edge cases I would have missed
>
> **The biggest surprise?** How much time AI saved on tedious tasks, freeing me to focus on design decisions and requirement interpretation.
>
> **But also:** I still had to read and understand every line. AI is not autopilot - it's a very fast junior developer who needs supervision."

**[TRANSITION]** → "Let me wrap up"

---

## Slide 6: Takeaways & Q&A (8:30 - 10:00)

### Visual
- Key takeaways list
- GitHub repo link
- CI badge (if available)

### Script

> "Key takeaways from this project:
>
> **1. AI amplifies, but doesn't replace, engineering judgment**
> - You still need to understand the code
> - You still make the architectural decisions
> - You still own the quality
>
> **2. Test-driven development matters even more with AI**
> - AI can generate buggy code with confident-sounding documentation
> - Tests are your safety net
> - 14 tests gave me confidence to trust AI output
>
> **3. Simple is better than complex**
> - Zero external dependencies (except pytest)
> - Plain CSV format
> - No database, no cloud, no API
> - **Result:** Works anywhere Python runs
>
> **4. Documentation is code**
> - Type hints
> - Docstrings  
> - README
> - This presentation
> - All generated with AI help, refined by human judgment
>
> **Project metrics:**
> - 14 tests passing
> - CI pipeline green
> - Runs on Python 3.8+
> - Zero dependencies for core functionality
> - Complete documentation
>
> **What I'd do differently:**
> - Add budget threshold warnings
> - Support date range filtering
> - Generate monthly trend reports
>
> **But I deliberately kept it simple for this project.**
>
> ---
>
> **Questions I'm ready to answer:**
> 1. How did you validate AI-generated code?
> 2. What was your testing strategy?
> 3. Why not use pandas/numpy?
> 4. How does CI/CD work?
> 5. What would you add next?
>
> ---
>
> **Thank you!**
>
> The code is on GitHub: [your-repo-link]
> All tests pass. The CI badge proves it.
> I'm happy to take questions."

---

## Backup Plan (If Demo Fails)

### If Live Demo Breaks

**SAY THIS:**
> "Looks like we hit a demo issue - this is exactly why I recorded a backup. Let me show you that instead."

**[PLAY PRE-RECORDED VIDEO]**

**[WHILE VIDEO PLAYS, NARRATE:]**
> "This shows the same workflow - reading the CSV, processing data, handling errors, running tests. Everything we just discussed."

---

## 📋 Pre-Presentation Checklist

- [ ] Test run the program (verify it works)
- [ ] Test run pytest (verify all tests pass)
- [ ] Create backup video (2-3 minutes of demo)
- [ ] Prepare sample CSV with intentional errors
- [ ] Have GitHub repo link ready
- [ ] Practice timing (should finish in 9-10 minutes)
- [ ] Prepare for Q&A (common questions below)

---

## ❓ Q&A Preparation

### Expected Question 1: "Why not use pandas?"
**Answer:**
> "Great question. Pandas would make this easier, but I chose not to use it for three reasons:
> 1. **Portability** - Python stdlib only means it works everywhere
> 2. **Learning** - I wanted to practice core Python patterns
> 3. **Simplicity** - This tool doesn't need pandas' power for 15 rows of data
>
> For a production tool with thousands of transactions, I'd absolutely use pandas."

### Expected Question 2: "How do you know AI's code is correct?"
**Answer:**
> "Three-layer validation:
> 1. **Read every line** - I understand what the code does
> 2. **Test with real data** - Not just AI's examples
> 3. **Unit tests** - 14 tests covering edge cases
>
> If I can't explain a line, I don't commit it."

### Expected Question 3: "What about the matplotlib issue?"
**Answer:**
> "Good catch. There's a conda DLL issue preventing chart generation - that's why the project works fine without it. Chart generation is optional. The core analysis works perfectly. This actually demonstrates good error handling - the tool warns you but doesn't crash."

### Expected Question 4: "Would you use AI again?"
**Answer:**
> "Absolutely, but with lessons learned:
> 1. Start with even more detailed requirements
> 2. Build tests FIRST, then have AI fill implementation
> 3. Iterate in smaller chunks rather than one big prompt
> 4. Always review with 'simplicity' lens - reject bloat
>
> AI is now part of my standard workflow, but I'm the architect."

---

## 🎥 Recording Tips (If Pre-Recording)

1. **Audio:** Use a decent microphone, minimize background noise
2. **Screen:** 1920x1080 resolution, large terminal font (16-18pt)
3. **Pace:** Speak slowly and clearly
4. **Cuts:** Edit out long waits (test running, etc.)
5. **Length:** Aim for 9-10 minutes total
6. **Backup:** Have slides as PDF in case video fails

---

## ⏱️ Timing Breakdown

- 0:00 - 1:00: Hook (Why this matters)
- 1:00 - 2:30: Architecture (How it's built)
- 2:30 - 5:30: Demo (Watch it work) ← **Longest section**
- 5:30 - 7:00: AI Collaboration (What AI did, what I decided)
- 7:00 - 8:30: Surprises (What I learned)
- 8:30 - 10:00: Takeaways & Q&A

**TOTAL: 10 minutes**

---

**Good luck! You've got this! 🚀**
