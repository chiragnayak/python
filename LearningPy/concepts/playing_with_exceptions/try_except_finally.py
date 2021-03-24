from LearningPy.concepts.playing_with_exceptions.Notification import Notification


def test_rail_replica():
    case_handler = None
    try:

        case_handler = Notification("Chirag is here!!")
        raise

    except Exception:
        print("\n\nUPDATE TEST FAILED")
        raise
    finally:

        print("Creating Case Processor Dumps...")

        case_handler.get_message()

        print("UPDATE TEST COMPLETE")


if __name__ == '__main__':
    test_rail_replica()
