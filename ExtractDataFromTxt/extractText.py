import matplotlib.pyplot as plt

with open("YoloLog.txt", "r") as file:
    lines = file.readlines()

count = 0
total_loss = []

for line in lines:
    if line.startswith("169846") and "100%" in line and "/249" in line:
        count += 1
        elements = line.split()

        # Access the box_loss and obj_loss
        box_loss = elements[5]
        obj_loss = elements[6]
        total = float(box_loss) + float(obj_loss)
        total_loss.append(total)

# print(total_loss)

epochs = len(total_loss)
rounds = list(range(1, epochs + 1))

plt.figure(figsize=(10, 6))
plt.plot(rounds, total_loss, marker="o", linestyle="-")
plt.title("Total loss vs epochs")
plt.xlabel("Epochs")
plt.ylabel("Total loss for Yolo")
plt.grid(True)
plt.yticks([0.02, 0.04, 0.06, 0.08, 0.10, 0.12])

# Show the graph or save it to a file
plt.show()
# print(count)
