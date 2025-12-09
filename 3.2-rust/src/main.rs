use std::fs;
use std::cmp::Ordering;

fn bank_largest_joltage_digit(slice: &[u8]) -> (usize, u8) {
    slice.iter()
        .enumerate()
        .map(|(idx, &value)| (idx, value - 48))
        .max_by(|(_, a), (_, b)| a.cmp(b).then(Ordering::Greater))
        .unwrap()
}

fn bank_largest_joltage(slice: &[u8]) -> u64 {
    let mut slice: &[u8] = slice;
    let mut final_value: u64 = 0;

    for i in 0..12 {
        let slice_end = slice.len() + i - 11;
        let (idx, value) = bank_largest_joltage_digit(&slice[0..slice_end]);
        final_value = final_value * 10 + value as u64;
        slice = &slice[idx+1..];
    }

    final_value
}

fn main() {
    let output = fs::read_to_string("input.txt")
        .expect("Failed to find input.txt file?")
        .split('\n')
        .filter(|x| !x.is_empty())
        .map(|x| bank_largest_joltage(x.as_bytes()))
        .sum::<u64>()
        ;

    println!("Largest joltage is: {}", output);
}
