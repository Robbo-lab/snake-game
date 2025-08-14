+
## **Setup (Before Class)**

1. Create a **GitHub classroom group repo** or a single shared repo.
2. Add a small project (HTML/JS or README-based).
3. Add **at least 3 starter commits**.
4. Include these instructions in the repo’s README.

---

## **Part 1 – Cloning and Staying Updated with `git pull`**

**Scenario:**
You’re joining a project that your team is already working on.

**Steps:**

1. Go into our Snake Game repo
- Students who have no copy **clone** the repo:

   ```bash
   git clone https://github.com/Robbo-lab/snake-game.git
   cd snake_game
   ```
2. Before making changes, they **pull** the latest work:

   ```bash
   git pull origin main
   ```
3. Discuss:

   * `git pull` = `git fetch` + `git merge` (auto-merges fetched changes into your local branch).
   * Use before starting work to avoid conflicts.

---

## **Part 2 – Branching and Initial Work**

**Scenario:**
Everyone works on different features in separate branches.

**Steps:**

1. Create a branch:

   ```bash
   git branch feature-<name>
   git checkout feature-<name>
   ```
2. Make a change, commit, and push:

   ```bash
   git add .
   git commit -m "Add feature for <name>"
   git push -u origin feature-<name>
   ```
3. Pull `main` updates before merging later:

   ```bash
   git checkout main
   git pull origin main
   ```

---

## **Part 3 – Merging and Conflict Resolution**

**Scenario:**
Two branches edit the same file. Merging will cause a conflict.

**Steps:**

1. Switch to `main` and **pull latest**:

   ```bash
   git checkout main
   git pull origin main
   ```
2. Merge your teammate’s branch:

   ```bash
   git merge feature-other
   ```
3. Resolve conflicts, then:

   ```bash
   git add .
   git commit
   ```

---

## **Part 4 – Using `git stash`**

**Scenario:**
You have unfinished work but need to pull changes from `main` urgently.

**Steps:**

1. Make changes but **don’t commit**.
2. Save work:

   ```bash
   git stash
   ```
3. Pull updates from `main`:

   ```bash
   git checkout main
   git pull origin main
   ```
4. Return to your branch and restore:

   ```bash
   git checkout feature-<name>
   git stash pop
   ```

---

## **Part 5 – Undoing Mistakes**

**Scenario 1 – Using `git reset`**
You committed locally but want to erase it.

```bash
git reset --hard HEAD~1
```

**Scenario 2 – Using `git revert`**
You pushed a mistake to `main` and must undo it safely.

```bash
git revert <commit_hash>
git push
```

---

## **Part 6 – Rebasing and Cleaning History**

**Scenario:**
You want cleaner commits before merging.

**Steps:**

1. Make 2–3 small commits in your branch.
2. Rebase:

   ```bash
   git pull origin main --rebase
   git rebase -i HEAD~3
   ```
3. Squash commits, then:

   ```bash
   git push --force
   ```

---

## **Wrap-up Challenge**

* Students must:

  1. Create a branch and commit a change.
  2. Pull updates from `main`.
  3. Merge their work without conflicts.
  4. Stash, pull, and restore.
  5. Reset a local commit.
  6. Revert a pushed commit.
  7. Rebase to clean history.

---

If you want, I can now **turn this into a printable classroom worksheet** where each step has:

* Commands to run.
* A “What happened?” box for students to fill in.
  That way, it’s ready to hand out and students actively record their learning.
