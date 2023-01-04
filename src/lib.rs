pub fn max_subarray(arr: &[i64], n: usize) -> &[i64] {
    let mut sum = i64::MIN;
    let mut left = 0;
    let mut right = arr.len();
    for i in 0..arr.len() {
        let j = i + n;
        if j > arr.len() {
            break;
        }
        let window_sum: i64 = arr[i..j].into_iter().sum();
        if window_sum > sum {
            sum = window_sum;
            left = i;
            right = j;
        }
    }
    &arr[left..right]
}

#[cfg(test)]
mod test_max_subarray {
    use super::*;

    #[test]
    fn examples() {
        assert_eq!(
            [1, 2, 3, 6],
            max_subarray(&[-4, 2, -5, 1, 2, 3, 6, -5, 1], 4)
        );
        assert_eq!([0, 5], max_subarray(&[1, 2, 0, 5], 2));
        assert_eq!([1, 2, 0, 5], max_subarray(&[1, 2, 0, 5], 15));
    }
}
