# Terraform Module Structure & Best Practices

---

## 🔹 1. High-Level Approach

Companies usually separate Terraform into:

- **Reusable modules** → Generic building blocks  
- **Environment configurations (roots)** → Actual deployments using modules  

---

## 🔹 2. Common Repository Strategies

### ✅ Option A: Monorepo (Common in Smaller Teams)

Single repo containing everything.
