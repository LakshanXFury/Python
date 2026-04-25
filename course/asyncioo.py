import asyncio

"""All three downloads happen at the same time!"""

async def download_file(name):
    print(f"Downloading {name}...")
    await asyncio.sleep(3)  # Simulates download time (non-blocking)
    print(f"Downloaded {name}")
    return f"{name}.txt"

async def main():
    print("Starting")

    # Start all downloads concurrently
    file1 = asyncio.create_task(download_file("file1"))
    file2 = asyncio.create_task(download_file("file2"))
    file3 = asyncio.create_task(download_file("file3"))

    await file1
    await file2
    await file3

    print("Finished")

asyncio.run(main())