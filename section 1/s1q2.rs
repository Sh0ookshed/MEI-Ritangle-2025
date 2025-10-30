//SECTION 1 , QUESTION2
use itertools::Itertools; // 0.14.0

fn dist(a: char, b: char) -> i32 {
    let line_dist = ((a as i32) - (b as i32)).abs();
    
    if line_dist < 13 {
        line_dist
    } else {
        26-line_dist
    }
}

fn main() {
    let word = ['r', 'i', 't', 'a', 'n', 'g', 'l', 'e'].to_vec();
    
    let mut shortest = 100000;
    let mut longest = 0;

    // perms    
    for p in word.iter().permutations(word.len()).unique() {
        let len: i32 = p.windows(2).map(|x| dist(**x.to_vec().first().unwrap(), **x.to_vec().last().unwrap())).sum();
        
        if len < shortest {
            shortest = len
        }
        if len > longest {
            longest = len
        }
    }
    
    println!("{}", shortest*longest)
}