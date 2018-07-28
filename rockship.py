arr = [3,7,1,3]
max_diff = -float("Inf")
for i in range(len(arr) - 1):
	max_diff = max(max_diff, max(arr[i+1:]) - arr[i])
print(max_diff)

def main(argv):
  input_dir = argv[2];
  _data, vocab, max_length = generate_data(input_dir)
  max_box = get_max_box(_data)
  newData = padding_ssd(_data, max_box)
  dataEncoder = encoderData(newData, vocab._vocab, max_length, max_box)
  with open(FLAGS.encoder_data_file, 'wb') as pickle_file:
    pickle.dump(dataEncoder, pickle_file, -1)

if __name__ == "__main__":
  assert len(sys.argv) >= 3, "Missing input"
  main(argv=sys.argv[2:])