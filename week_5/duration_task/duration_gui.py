import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

AVG_MONTH_DAYS = 30.44  # average month length used in CLI version

def convert_days_to_unit(days: int, unit: str) -> tuple[float, str]:
    """Convert integer day count to the requested unit ('d', 'w', 'm')."""
    unit = unit.lower()
    if unit == "w":
        return round(days / 7, 2), "weeks"
    if unit == "m":
        return round(days / AVG_MONTH_DAYS, 2), "months"
    return days, "days"

# --- GUI callbacks ---

def calculate_duration():
    """Calculate duration between dates and display it in the selected unit."""
    try:
        start_np = np.datetime64(start_calendar.get_date(), "D")
        if use_today_var.get():
            end_np = np.datetime64(np.datetime64("today", "D"), "D")
        else:
            end_np = np.datetime64(end_calendar.get_date(), "D")

        duration_days = int((end_np - start_np).astype(int))
        if duration_days < 0:
            messagebox.showwarning("Invalid range", "End date must be on or after the start date.")
            result_var.set("—")
            return

        unit_key = unit_var.get()  # 'd' | 'w' | 'm'
        value, unit_name = convert_days_to_unit(duration_days, unit_key)
        result_var.set(f"{value} {unit_name}")

        # Optional: log result
        if log_var.get():
            with open("duration_log.txt", "a", encoding="utf-8") as f:
                f.write(f"{start_np},{end_np},{value} {unit_name}\n")

    except Exception as exc:  # defensive, in case of unexpected values
        messagebox.showerror("Error", f"Could not calculate duration.\n\nDetails: {exc}")
        result_var.set("—")

def toggle_end_date():
    """Enable/disable end date calendar when 'Use today' is toggled."""
    if use_today_var.get():
        end_calendar.set_date(np.datetime64("today", "D").astype(str))
        end_calendar.config(state="disabled")
    else:
        end_calendar.config(state="normal")

# Build GUI 

root = tk.Tk()
root.title("Date Duration Calculator")

# Start Date
tk.Label(root, text="Start Date:").grid(row=0, column=0, padx=10, pady=6, sticky="e")
start_calendar = DateEntry(root, date_pattern="yyyy-mm-dd", width=18)
start_calendar.grid(row=0, column=1, padx=10, pady=6, sticky="w")

# End Date controls
use_today_var = tk.BooleanVar(value=True)
tk.Checkbutton(
    root,
    text="Use today's date as end date",
    variable=use_today_var,
    command=toggle_end_date
).grid(row=1, column=0, columnspan=2, padx=10, pady=4, sticky="w")

tk.Label(root, text="End Date:").grid(row=2, column=0, padx=10, pady=6, sticky="e")
end_calendar = DateEntry(root, date_pattern="yyyy-mm-dd", width=18)
end_calendar.grid(row=2, column=1, padx=10, pady=6, sticky="w")

# Unit selection (days/weeks/months)
tk.Label(root, text="Show as:").grid(row=3, column=0, padx=10, pady=6, sticky="e")
unit_var = tk.StringVar(value="d")
unit_frame = tk.Frame(root)
unit_frame.grid(row=3, column=1, padx=10, pady=6, sticky="w")
tk.Radiobutton(unit_frame, text="Days",   value="d", variable=unit_var).pack(side="left")
tk.Radiobutton(unit_frame, text="Weeks",  value="w", variable=unit_var).pack(side="left")
tk.Radiobutton(unit_frame, text="Months", value="m", variable=unit_var).pack(side="left")

# Optional logging
log_var = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Log result to duration_log.txt", variable=log_var).grid(
    row=4, column=0, columnspan=2, padx=10, pady=4, sticky="w"
)

# Calculate button
tk.Button(root, text="Calculate Duration", command=calculate_duration, width=28).grid(
    row=5, column=0, columnspan=2, pady=10
)

# Result display
tk.Label(root, text="Result:").grid(row=6, column=0, padx=10, pady=6, sticky="e")
result_var = tk.StringVar(value="—")
tk.Label(root, textvariable=result_var).grid(row=6, column=1, padx=10, pady=6, sticky="w")

# Initialise end date as today and disable widget (since checkbox is on)
end_calendar.set_date(np.datetime64("today", "D").astype(str))
end_calendar.config(state="disabled")

root.mainloop()
