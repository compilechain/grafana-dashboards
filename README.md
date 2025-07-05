Here's an improved and structured version of your README for the Grafana dashboards project:

# grafana-dashboards

Welcome to the **grafana-dashboards** repository! This project is dedicated to managing Grafana dashboard JSON exports and provisioning configurations in a version-controlled environment. This README outlines our project overview, journey, repository structure, key configurations, workflow, and contribution guidelines.

---

## 🛠️ Project Overview

In this repository, we maintain all Grafana dashboard JSON exports and their corresponding provisioning configurations. By utilizing version control, we achieve:

- **Reproducibility:** Easily redeploy dashboards on any Grafana instance.
- **Auditability:** Track every change made to dashboards and provisioning settings.
- **Collaboration:** Facilitate team reviews, comments, and extensions through pull requests.

---

## 🚀 Our Journey

1. **Installed Git for Windows** using SChannel for TLS, leveraging the Windows certificate store.
2. **Initialized a local Git repository** within the Grafana provisioning folder.
3. **Created a `.gitignore` file** to exclude editor and temporary files (e.g., `*.swp`, `*~`).
4. **Added dashboard JSON files** and committed the initial exports.
5. **Created `providers.yaml`** with `disableDeletion: true` to prevent unwanted dashboard removal.
6. **Established fast-forward-only pulls** to maintain a linear commit history and avoid merge commits.
7. **Configured Grafana file-based provisioning** through `custom.ini` overrides.
8. **Verified** that Grafana imports the latest JSON files upon service restart and through automated pulls.

---

## 📂 Repository Structure

```
/ (root)
├─ .gitignore           # Ignores editor and temporary files
├─ README.md            # This file
├─ providers.yaml       # Provisioning configuration for dashboards
├─ dashboards/          # Directory containing all exported JSON dashboard definitions
│    ├─ my-dashboard.json
│    └─ ...
```

---

## ⚙️ Key Configuration Files

### `.gitignore`

```gitignore
*.swp
*~
```

### `providers.yaml` (located in `/conf/provisioning/dashboards/`)

```yaml
providers:
  - name: 'my-dashboards'
    type: file
    updateIntervalSeconds: 30
    disableDeletion: true  # Prevents JSON removal from deleting dashboards
    options:
      path: C:/Program Files/GrafanaLabs/grafana/conf/provisioning/dashboards
```

### `custom.ini` (Grafana configuration override)

```ini
[feature_toggles]
provisioning = true  # Enables file-based provisioning
```

---

## 🔄 Workflow & Automation

1. **Pushing Changes:**

   Use the following commands to add and commit changes:

   ```bash
   git add <files>
   git commit -m "<type>: <description>"
   git push origin master
   ```

2. **Automated Sync:**

   - Set up **Windows Task Scheduler** to run `git pull` every hour or at startup.
   - Use the fast-forward-only configuration (`git config pull.ff only`) to ensure clean updates.

3. **Grafana Restart:**

   A restart is not required if provisioning automatically picks up new JSON files.

---

## 📜 License

This repository is licensed under the **MIT License**, a permissive license that allows our dashboards to be freely used and modified within the organization.

---

## 💬 Contribution

We welcome contributions! Please submit issues or pull requests with clear commit messages prefixed with `feat:`, `chore:`, or `fix:`. Remember to include inline comments in YAML/JSON snippets for clarity.

---

Thank you for being part of the **grafana-dashboards** project! Let's work together to create and maintain excellent Grafana dashboards.