def main() -> None:
    project_name = "Business Hard 40"
    app_version = "0.1.0"
    is_active = True
    max_items = 100
    average_latency_ms = 12.5

    print("=== App Settings (Sample) ===")
    print(f"Project: {project_name}")
    print(f"Version: {app_version}")
    print(f"Active: {is_active}")
    print(f"Max items: {max_items}")
    print(f"Avg latency: {average_latency_ms} ms")

    print("\n=== Types ===")
    print(type(project_name))
    print(type(app_version))
    print(type(is_active))
    print(type(max_items))
    print(type(average_latency_ms))


if __name__ == "__main__":
    main()
