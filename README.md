# grafana-dashboards
Remote repo for Git
# grafana-dashboards

Welcome to the **grafana-dashboards** repository! This README captures our journey, configuration steps, and best practices so that our team stays organized and cohesive.

---

## 🛠️ Project Overview

We manage all Grafana dashboard JSON exports and provisioning configuration in this Git repository. By version-controlling dashboards and their provisioning YAML, we ensure:

* **Reproducibility:** Dashboards can be redeployed on any Grafana instance.
* **Auditability:** Every change to dashboards or provisioning settings is tracked.
* **Collaboration:** Teammates can review, comment, and extend dashboards via pull requests.

---

## 🚀 Our Journey

1. **Installed Git for Windows** using SChannel for TLS (leveraging Windows certificate store).
2. **Initialized a local Git repo** under the Grafana provisioning folder.
3. **Created `.gitignore`** to exclude editor and temp files (`*.swp`, `*~`).
4. **Added dashboard JSONs** and committed initial exports.
5. **Created `providers.yaml`** with `disableDeletion: true` to prevent unwanted dashboard removal.
6. **Established fast-forward-only pulls** to keep history linear and avoid merge commits.
7. **Configured Grafana file-based provisioning** via `custom.ini` overrides.
8. **Verified** Grafana imports the latest JSONs on service restart and via automated pulls.

---

## 📂 Repository Structure

```
/ (root)
├─ .gitignore           # ignores editor/temp files
├─ README.md            # this file
├─ providers.yaml       # provisioning config for dashboards
├─ dashboards/          # all exported JSON dashboard definitions
│    ├─ my-dashboard.json
│    └─ ...
```

---

## ⚙️ Key Configuration Files

* **`.gitignore`**

  ```gitignore
  *.swp
  *~
  ```
* **`providers.yaml`** (in `/conf/provisioning/dashboards/`)

  ```yaml
  providers:
    - name: 'my-dashboards'
      type: file
      updateIntervalSeconds: 30
      disableDeletion: true  # prevents JSON removal from deleting dashboards
      options:
        path: C:/Program Files/GrafanaLabs/grafana/conf/provisioning/dashboards
  ```
* **`custom.ini`** (Grafana config override)

  ```ini
  [feature_toggles]
  provisioning = true  # enables file-based provisioning
  ```

---

## 🔄 Workflow & Automation

1. **Push changes:**

   ```bash
   git add <files>
   git commit -m "<type>: <description>"
   git push origin master
   ```
2. **Automated sync:**

   * **Windows Task Scheduler** runs `git pull` every hour (or at startup).
   * **Fast-forward-only** configuration (`git config pull.ff only`) ensures clean updates.
3. **Grafana restart** not required if provisioning picks up new JSONs automatically.

---

## 📜 License

This repository is licensed under the **MIT License**—a permissive, team-friendly license that ensures our dashboards can be freely used and modified within the organization.

---

## 💬 Contribution

Feel free to submit issues or pull requests. Use clear commit messages prefixed with `feat:`, `chore:`, or `fix:`. Always include inline comments in YAML/JSON snippets for clarity.
