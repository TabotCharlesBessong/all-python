#turtle.done() (Does not close window nor reset anything.) A synonym for turtle.mainloop()

#turtle.clear() Deletes everything this turtle has drawn (not just the last thing). Otherwise doesn't affect the state of the turtle.

#turtle.reset() Does a turtle.clear() and then resets this turtle's state (i.e. direction, position, etc.)

#turtle.clearscreen() aka turtle.Screen().clear() Deletes all drawing and all turtles, reseting the window to it's original state.

#turtle.resetscreen() aka turtle.Screen().reset() Resets all turtles on the screen to their initial state.

#turtle.bye() aka turtle.Screen().bye() Closes the turtle graphics window. I don't see a way to use any turtle graphics commands after this is invoked.

#turtle.exitonclick() aka turtle.Screen().exitonclick() After binding the screen click event to do a turtle.Screen().bye() invokes turtle.Screen().mainloop()