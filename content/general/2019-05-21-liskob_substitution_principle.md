Tags: ruby, design principles, solid

# Idea:

"Software entities should be open for extension, but closed for modification."

Software entities can be functions or classes. In case of classes, design them so you can avoid modify their existing codes later.

# Exmaple in Ruby:

```ruby
class Rectangle
  attr_accessor :width, :height

  def initialize(width, height)
    @width = width
    @height = height
  end
end


class Circle
  attr_accessor :radius

  def initialize(radius)
    @radius = radius
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

Later when you want to add more shapes, you have to modify method `run` of `Calculator`. Design them like these instead:

```ruby
class Rectangle
  attr_accessor :width, :height

  def initialize(width, height)
    @width = width
    @height = height
  end

  def area
    @width * @height
  end
end


class Circle
  attr_accessor :radius

  def initialize(radius)
    @radius = radius
  end

  def area
    @radius * @radius * 3.14
  end
end


class Calculator

  def self.run(shape)
    return shape.area
  end
end
```

The less modification on existing codes, the less trouble you will get.
