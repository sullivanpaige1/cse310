use std::io;

fn ask(question: &str) -> String {
    println!("{}", question);

    let mut answer = String::new();

    io::stdin()
        .read_line(&mut answer)
        .expect("Could not read input");

    answer.trim().to_string()
}

fn main() {
    println!("🎃 HALLOWEEN MAD LIBS 🎃\n");
    

    println!("Welcome to the Halloween Mad Libs! Let's create a spooky story together! Please answer the following questions:\n");

    let name = ask("Enter a person's name:");
    let adjective = ask("Enter an adjective:");
    let place = ask("Enter a spooky place:");
    let animal = ask("Enter an animal:");
    let sound = ask("Enter a funny sound:");
    let verb = ask("Enter a verb:");
    let food = ask("Enter a food:");
    let number = ask("Enter a number:");
    let object = ask("Enter an object:");
    let feeling = ask("Enter a feeling:");

    println!("\n🕸️ YOUR HALLOWEEN STORY 🕸️\n");

    println!(
        "One dark and {} Halloween night, {} decided to visit {}.",
        adjective, name, place
    );

    println!(
        "The moon was shining brightly, and the wind sounded like {}.",
        sound
    );

    println!(
        "As {} walked through the front door, a mysterious {} appeared!",
        name, animal
    );

    println!(
        "The creature told {} that they had to {} before midnight.",
        name, verb
    );

    println!(
        "To complete the challenge, {} had to find {} pieces of {}.",
        name, number, object
    );

    println!(
        "Along the way, {} found a giant bowl of {}.",
        name, food
    );

    println!(
        "After eating it, {} suddenly felt very {}.",
        name, feeling
    );

    println!(
        "The {} chased {} through the hallway while screaming, '{}!'",
        animal, name, sound
    );

    println!(
        "Finally, {} escaped the haunted house and went home with the {}.",
        name, object
    );

    println!(
        "\nEveryone agreed it was the most {} Halloween ever!",
        adjective
    );

    println!("🎃 THE END 🎃");
}