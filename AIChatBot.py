from asyncio import run
from GPTs import gpt3, gpt4, alpaca_7b, falcon_40b

def select_model():
    models = {
        "gpt3": gpt3,
        "gpt4": gpt4,
        "alpaca_7b": alpaca_7b,
        "falcon_40b": falcon_40b,
    }

    print("\nAvailable Models:\n")
    model_names = list(models.keys())
    for i in range(len(model_names)):
        print(str(i + 1) + ". " + model_names[i])

    return models[model_names[int(input("\nYour Choice: ")) - 1]]



model = select_model()


async def main():
    while True:
        prompt = input("\n👦: ")
        try:
            resp = await model.Completion().create(prompt)
            print(f"🤖: {resp}")
        except Exception as e:
            print(f"🤖: {e}")


run(main())
