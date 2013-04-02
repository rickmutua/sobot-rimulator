#!/usr/bin/python
# -*- Encoding: utf-8 -*

class Pose:

  def __init__( self, x, y, phi ):
    self.x = x
    self.y = y
    self.phi = phi

  def unpack( self ):
    return self.x, self.y, self.phi 
