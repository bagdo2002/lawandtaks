const currentYear = new Date().getFullYear();
const name = prompt("რა გქქვია?");
let age = parseInt(prompt("რამდენი წლის ხარ?"));


//ვალიდაცია
while (isNaN(age) || age < 0) {
  age = parseInt(prompt("არასწორი მონაცემი,გთხოვთ სწორი რიცხვი შეიყვანოთ."));
}

const yearOfBirth = currentYear - age;
const yearOfHundredthBirthday = yearOfBirth + 100;

alert(`${name}, შენ გახდები 100 წლის ${yearOfHundredthBirthday}.`);


