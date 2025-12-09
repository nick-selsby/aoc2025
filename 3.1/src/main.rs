use std::fs;
use std::cmp::Ordering;

fn bank_largest_joltage(slice: &[u8]) -> u8 {
    let (max_a_idx, max_a) = slice
        [..slice.len()-1]
        .iter()
        .enumerate()
        .max_by(|(_, a), (_, b)| a.cmp(b).then(Ordering::Greater))
        .unwrap()
        ;

    let max_b = slice
        [max_a_idx+1..]
        .iter()
        .max()
        .unwrap()
        ;

    println!("{} {}{}", max_a_idx, max_a - 48, max_b - 48);
    (max_a - 48) * 10 + (max_b - 48)
}

fn main() {
    let output: i32 = fs::read_to_string("input.txt")
        .expect("Failed to find input.txt file?")
        .split('\n')
        .filter(|x| !x.is_empty())
        .map(|x| bank_largest_joltage(x.as_bytes()))
        .map(|x| x as i32)
        .sum::<i32>()
        ;

    println!("Largest joltage is: {}", output);
}
