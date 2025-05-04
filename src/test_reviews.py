import json

with open("reviews/reviews.json", encoding="utf-8") as f:
    reviews = json.load(f)

print("\nTÜM BAŞLIKLAR:\n", list(reviews.keys()))

title = "Inception"  # örnek film adı

print(f"\n{title} için yorumlar:")
for r in reviews.get(title, []):
    print("----")
    print("username:", r.get("username"))
    print("score:", r.get("score"))
    print("comment:", r.get("comment"))
    print("date:", r.get("date"))
