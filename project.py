import json

def main():
    print("Welcome to Hybrid Dataset‑Driven CLI for PC Build Recommendations")
    choice = input("Build by (1) Budget or (2) Custom Configuration? ")
    if choice == "1":
        budget_mode()
    else:
        custom_mode()

def load_parts():
    with open("parts.json", "r") as f:
        return json.load(f)

def load_custom_parts():
    with open("custom_parts.json", "r") as f:
        return json.load(f)

# ---------------- BUDGET MODE ----------------
def budget_mode():
    budget = int(input("Enter your budget (20000 - 60000): "))
    usage = input("Usage type (Gaming/Office/Student): ")
    builds = recommend_by_budget(budget, usage)
    display_table(builds)
    save_choice = input("Do you want to save this build? (y/n): ")
    if save_choice.lower() == "y":
        save_build(builds)

def recommend_by_budget(budget, usage):
    parts_data = load_parts()
    builds = []
    if usage not in parts_data:
        return [{"Error": "Usage type not found"}]

    for tier_name, build in parts_data[usage].items():
     if build.get("Price") == budget:
        builds.append({"Tier": tier_name, **build})
    return builds

# ---------------- CUSTOM MODE ----------------
def custom_mode():
    custom_data = load_custom_parts()

    usage = input("What will you use this PC for? (Gaming/Office/Hybrid): ")

    print("Intel CPUs: strong single-core, great for productivity.")
    print("AMD CPUs: more cores, better multitasking and gaming.")
    cpu_brand = input("Do you prefer Intel or AMD? ")
    if cpu_brand.lower() == "intel":
        series = input("Choose Intel series (i3/i5/i7): ")
        cpu = f"Intel {series}"
    else:
        series = input("Choose AMD series (Ryzen 3/5/7): ")
        cpu = f"AMD {series}"

    cpu_info = custom_data["CPU"].get(cpu, {"Price": "Unknown", "Link": "N/A"})

    print("NVIDIA GPUs: ray tracing, DLSS support.")
    print("AMD GPUs: better price/performance.")
    gpu_choice = input("Choose GPU (GTX 1650/RTX 3060/RTX 3070/RX 6600/RX 6700): ")
    gpu_info = custom_data["GPU"].get(gpu_choice, {"Price": "Unknown", "Link": "N/A"})

    ram_choice = input("How much RAM? (8GB/16GB/32GB): ")
    ram_info = custom_data["RAM"].get(ram_choice, {"Price": "Unknown", "Link": "N/A"})

    storage_choice = input("Storage type? (256GB SSD/512GB SSD/1TB NVMe): ")
    storage_info = custom_data["Storage"].get(storage_choice, {"Price": "Unknown", "Link": "N/A"})

    build = {
        "Tier": "Custom",
        "CPU": cpu,
        "GPU": gpu_choice,
        "RAM": ram_choice,
        "Storage": storage_choice,
        "PSU": "650W Bronze",
        "Motherboard": "B550 ATX",
        "Price": "Estimated",
        "ComponentPrices": {
            "CPU": cpu_info["Price"],
            "GPU": gpu_info["Price"],
            "RAM": ram_info["Price"],
            "Storage": storage_info["Price"],
            "PSU": 4000,
            "Motherboard": 6000
        },
        "Links": {
            "CPU": cpu_info["Link"],
            "GPU": gpu_info["Link"],
            "RAM": ram_info["Link"],
            "Storage": storage_info["Link"],
            "PSU": "https://www.amazon.com/s?k=650W+PSU",
            "Motherboard": "https://www.amazon.com/s?k=B550+Motherboard"
        }
    }
    display_table([build])
    save_choice = input("Do you want to save this build? (y/n): ")
    if save_choice.lower() == "y":
        save_build([build])

# ---------------- COMMON FUNCTIONS ----------------
def display_table(builds):
    print("\n=== Build Comparison ===")
    headers = ["Tier", "CPU", "GPU", "RAM", "Storage", "PSU", "Motherboard", "Price"]
    print("{:<15} {:<20} {:<15} {:<10} {:<15} {:<15} {:<20} {:<10}".format(*headers))
    for build in builds:
        print("{:<15} {:<20} {:<15} {:<10} {:<15} {:<15} {:<20} {:<10}".format(
            build.get("Tier", "-"),
            build.get("CPU", "-"),
            build.get("GPU", "-"),
            build.get("RAM", "-"),
            build.get("Storage", "-"),
            build.get("PSU", "-"),
            build.get("Motherboard", "-"),
            build.get("Price", "-")
        ))

        if "ComponentPrices" in build:
            print("\n--- Component Prices ---")
            for comp, price in build["ComponentPrices"].items():
                print(f"{comp}: ₹{price}")

        if "Links" in build:
            print("\n--- Component Links ---")
            for comp, link in build["Links"].items():
                print(f"{comp}: {link}")
            print("\n")

def save_build(builds):
    with open("build.json", "w") as f:
        for build in builds:
            f.write(json.dumps(build, indent=4))
            f.write("\n")
    print("Build saved to build.json")

if __name__ == "__main__":
    main()
