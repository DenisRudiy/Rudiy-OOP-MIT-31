class Length {
  static allData = [];
  static totalLengths = 0;

  static getTotalLengths() {
    return Length.totalLengths;
  }

  constructor(value, type) {
    this.value = value;
    this.type = type;
    Length.allData.push(this);
    Length.totalLengths++;
  }

  write() {
    console.log(`Length is: ${this.value} ${this.type}`);
  }

  add(number) {
    this.value += number;
    console.log(`Length is: ${this.value} ${this.type}`);
  }

  subtract(number) {
    if (this.value >= number) {
      this.value -= number;
      console.log(`Length is: ${this.value} ${this.type}`);
    } else {
      console.log("Warning! Length less than zero!");
    }
  }

  multiply(number) {
    this.value *= number;
    console.log(`Length is: ${this.value} ${this.type}`);
  }

  divide(number) {
    if (number !== 0) {
      this.value /= number;
      console.log(`Length is: ${this.value} ${this.type}`);
    } else {
      console.log("Warning! You are trying to divide by zero!");
    }
  }

  round(direction) {
    if (direction === "up") {
      this.value = Math.ceil(this.value);
      console.log(`Length is: ${this.value} ${this.type}`);
    }
    if (direction === "down") {
      this.value = Math.floor(this.value);
      console.log(`Length is: ${this.value} ${this.type}`);
    }
  }
}

// * Create "Lengths"
const length1 = new Length(5, "meters");
const length2 = new Length(1, "santimeters");
const length3 = new Length(3, "milimeters");

// * Make operations
length1.write();
length1.add(3);
length1.subtract(2);
length1.multiply(3);
length1.divide(4);
length1.round("down");

length2.write();
length2.divide(2);
length2.round("up");

console.log("\nTotal Lengths:", Length.getTotalLengths());

console.log("\n");
for (const item of Length.allData) {
  console.log(`Length: ${item.value} ${item.type}`);
}
