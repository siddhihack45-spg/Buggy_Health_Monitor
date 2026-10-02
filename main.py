
from sensors import SensorData
from detector import BuggyDetector


def main():
    detector = BuggyDetector()

    while True:
        print("\n==============================")
        print(" BUGGY HEALTH MONITOR")
        print("==============================")
        print("1. Train Random Forest")
        print("2. Load saved model")
        print("3. Predict buggy condition")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                detector.train()
                detector.save()

            elif choice == "2":
                detector.load()

            elif choice == "3":
                print("\nEnter sensor readings:")

                engine_temp = float(
                    input("Engine temperature: ")
                )
                vibration = float(
                    input("Vibration: ")
                )
                suspension = float(
                    input("Suspension: ")
                )

                buggy = SensorData(
                    engine_temp,
                    vibration,
                    suspension
                )

                buggy.display()

                condition, confidence = detector.predict(
                    buggy.get_readings()
                )

                print("\n--- PREDICTION ---")
                print("Condition:", condition)
                print("Model confidence:", confidence, "%")

            elif choice == "4":
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Enter 1, 2, 3 or 4.")

        except FileNotFoundError:
            print("No saved model found. Train the model first.")

        except (ValueError, TypeError, RuntimeError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()