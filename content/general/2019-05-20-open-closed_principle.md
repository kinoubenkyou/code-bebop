Tags: ruby, design principles, solid
Status: draft

# Idea:

"Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."

Overiding methods in extended classes should not have unexpected effect on the base classes.

# Example in Ruby:

```ruby
class Square < Rectangle
  def initialize(side)
    @width = side
    @height = side
  end

  def width=(width)
    @width = width
    @height = width
  end

  def height=(height)
    @height = height
    @width = height
  end
end


class Transformer
  def self.resize_by_area_through_width(rectangle, new_area)
    rectangle.width = new_area.to_f / rectangle.height
  end
end
```

The writer methods in `Square` unexpectedly modify the other attributes. This makes method `resize_by_area_through_width` of `Transformer` works incorrectly on `Square` object. Thus, `Square` should not extend from `Rectangle`.
