def fragmentation(total_memory, used_memory):
    internal = total_memory - used_memory
    print("\nFragmentation Analysis")
    print(f"Total Memory: {total_memory}")
    print(f"Used Memory: {used_memory}")
    print(f"Internal Fragmentation: {internal}")

    # update 4