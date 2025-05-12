# Memento Pattern

## 📖 Definition

The **Memento Pattern** is a behavioral design pattern that allows capturing and externalizing an object's internal state so that it can be restored later, **without violating encapsulation**.

In simpler terms, it helps an object save its state at a particular moment and restore it later if needed — like an **undo** feature.

---

## ❓ Why We Need It

- **Undo/Redo Functionality**  
  In applications like text editors, games, or design tools, users expect the ability to undo their last changes. The Memento Pattern provides a clean way to implement this feature.

- **State Management Without Breaking Encapsulation**  
  It allows saving and restoring an object's internal state **without exposing its internal structure** to the outside world.

- **Temporary State Checkpointing**  
  It's useful for storing temporary states before making complex or risky changes.

- **Rollback Support in Transactions**  
  In database systems or business logic workflows, you may want to roll back to a previous state if something goes wrong.

---

## 📦 Common Use Cases

- Text editors (undo/redo)
- Drawing applications (canvas state)
- Game engines (save checkpoints or game states)
- Database transactions (rollback functionality)
- Form wizards (go back to a previous step with retained data)
- Version control systems (track changes to objects)

---

## 🧠 Benefits

- Preserves object encapsulation
- Makes state-saving and restoration easy and modular
- Simplifies implementation of undo mechanisms
- Helps separate concerns between state management and core logic

---

## ⚠️ When Not to Use

- When object state is too large or complex — storing many snapshots can consume a lot of memory.
- If changes are frequent and mementos are created too often — can reduce performance.

---

## ✅ Summary

The Memento Pattern is essential when you want to save and restore object states cleanly and safely, especially when implementing undo or rollback functionality. It's a simple yet powerful tool for keeping your applications robust and user-friendly.

