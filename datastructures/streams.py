def joinStreams():
    i = int(input("Enter the number of the stream you want to join with the stream to it's right: ")) - 1
    new_stream_flow = stream_flows.pop(i) + stream_flows.pop(i)
    stream_flows.insert(i, new_stream_flow)

def slipStreams():
    i = int(input("Enter the number of the stream you want to split: ")) - 1
    left_split_percent = (float(input("Enter the split percentage: "))) / 100
    original_stream = stream_flows.pop(i)
    left_stream = original_stream * left_split_percent
    right_stream = original_stream * (1 - (left_split_percent))
    stream_flows.insert(i, left_stream)
    stream_flows.insert(i+1, right_stream)

stream_amount = int(input("Enter the number of streams: "))
stream_flows = []
for i in range(stream_amount):
    stream_flows.append(float(input(f"Enter stream #{i+1}'s flow: "))) 

command = 0
while command != 77:
    command = int(input("Enter a number (77 to stop, 88 to join, 99 to split): "))
    if command == 88:
        joinStreams()
    elif command == 99:
        slipStreams()

for i in range(len(stream_flows)):
    print(f"Stream #{i+1}'s flow is {round(stream_flows[i])}")
