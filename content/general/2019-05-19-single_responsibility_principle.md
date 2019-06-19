Tags: ruby, design principles, solid

# Idea:

"There should never be more than one reason for a class to change."

A class should have codes for only one thing.

# Example in Ruby:

```ruby
class Informer
  def self.run(shape)
    # calculate
    if shape.is_a? Rectangle
      area = shape.width * shape.height
    elsif shape.is_a? Circle
      area = shape.radius * shape.radius * 3.14
    end

    # output
    puts "area = #{area}"
  end
end
```

It has codes for two things: calculating and outputing. Break it into two classes:

```ruby
class Informer
  def self.run(shape)
    area = Calculator.run(shape)
    puts "area = #{area}"
  end
end


class Calculator
  def self.run(shape)
    area = shape.width * shape.height if shape.is_a? Rectangle
    area = shape.radius * shape.radius * 3.14 if shape.is_a? Circle
    return area
  end
end
```

Later when you need the calculation logic, there's a better chance you can find it in the code base.
