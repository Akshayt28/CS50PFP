import os
import json
import pytest
from project import recommend_by_budget, custom_mode, display_table, save_build

# ---------- Budget Mode Tests ----------

def test_budget_gaming_entry():
    builds = recommend_by_budget(20000, "Gaming")
    assert builds[0]["CPU"] == "AMD Ryzen 3 3200G (with Vega 8 Graphics)"
    assert builds[0]["Price"] == 20000

def test_budget_gaming_mid():
    builds = recommend_by_budget(25000, "Gaming")
    assert builds[0]["GPU"] == "Integrated GPU: Radeon Vega 8"
    assert "ComponentPrices" in builds[0]

def test_budget_office_basic():
    builds = recommend_by_budget(25000, "Office")
    assert builds[0]["GPU"] == "Integrated"
    assert builds[0]["ComponentPrices"]["CPU"] == 8000

def test_budget_student_entry():
    builds = recommend_by_budget(20000, "Student")
    assert "Pentium" in builds[0]["CPU"]

# ---------- Custom Mode Tests ----------

def test_custom_mode_function_exists():
    assert callable(custom_mode)

def test_display_table_prints(capsys):
    builds = [{
        "Tier":"Test",
        "CPU":"Intel i5",
        "GPU":"RTX 3060",
        "RAM":"16GB",
        "Storage":"512GB SSD",
        "PSU":"650W",
        "Motherboard":"B550",
        "Price":60000,
        "Links":{"CPU":"link"},
        "ComponentPrices":{"CPU":12000,"GPU":25000}
    }]
    display_table(builds)
    captured = capsys.readouterr()
    assert "Intel i5" in captured.out
    assert "Component Prices" in captured.out

def test_save_build_creates_file(tmp_path):
    builds = [{
        "Tier":"Test",
        "CPU":"Intel i5",
        "GPU":"RTX 3060",
        "RAM":"16GB",
        "Storage":"512GB SSD",
        "PSU":"650W",
        "Motherboard":"B550",
        "Price":60000,
        "Links":{"CPU":"link"},
        "ComponentPrices":{"CPU":12000,"GPU":25000}
    }]
    file_path = tmp_path / "build.json"
    os.chdir(tmp_path)
    save_build(builds)
    assert file_path.exists()