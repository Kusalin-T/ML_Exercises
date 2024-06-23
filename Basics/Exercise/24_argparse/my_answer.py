import argparse
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--physics', help="physic score")
    parser.add_argument('--chemistry', help="chemistry score")
    parser.add_argument('--maths', help="maths score")
    args = parser.parse_args()
    try:
        print(f"Average: {(int(args.physics)+int(args.chemistry)+int(args.maths))/3}")
    except Exception:
        print('oops')