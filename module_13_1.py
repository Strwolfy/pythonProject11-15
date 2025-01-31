import asyncio

async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):  # Поднимаем 5 шаров
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна силе
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    # Создаем три задачи с разными силачами
    tasks = [
        asyncio.create_task(start_strongman('Pasha', 3)),
        asyncio.create_task(start_strongman('Denis', 4)),
        asyncio.create_task(start_strongman('Apollon', 5))
    ]
    await asyncio.gather(*tasks)  # Ожидаем завершения всех задач

if __name__ == "__main__":
    asyncio.run(start_tournament())
