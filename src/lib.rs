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

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}
pub struct Solution;

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }

    fn append(&mut self, val: i32) {
        let new = Some(Box::new(ListNode::new(val)));
        match self.next {
            None => self.next = new,
            Some(_) => {
                let next = self.next.as_mut().unwrap();
                next.append(val);
            }
        }
    }

    fn to_vec(self) -> Vec<i32> {
        let mut result: Vec<i32> = vec![self.val];

        let mut head = &self;

        loop {
            let next = &head.next;
            if next.is_none() {
                break;
            }
            let n = next.as_ref().unwrap();
            result.push(n.val);

            head = n;
        }

        result
    }
}

impl Solution {
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() {
            return None;
        };

        let mut head = head.unwrap();
        if head.next.is_none() {
            return Some(head);
        };

        let mut new_head = head.next.unwrap();
        head.next = Solution::swap_pairs(new_head.next);
        new_head.next = Some(head);

        Some(new_head)
    }
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

    #[test]
    fn swap_pairs() {
        let mut head = ListNode::new(1);
        for i in 2..5 {
            head.append(i);
        }

        let result = Solution::swap_pairs(Some(Box::new(head)));
        let actual = result.unwrap().to_vec();
        let expected = vec![2, 1, 4, 3];
        assert_eq!(actual, expected)
    }
}
