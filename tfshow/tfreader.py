#!/usr/bin/env python

# Copyright 2022 daohu527 <daohu527@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from pycyber import cyber
from modules.transform.proto.transform_pb2 import TransformStampeds


# todo(zero): read from tf will need multi-threaded and resident in the background

class TfReader(Object):
  def __init__(self, tfshow):
    self.node = cyber.Node("tf_reader")
    self.node.create_reader("/tf", TransformStampeds, self.tf_callback)
    self.node.create_reader("/tf", TransformStampeds, self.tf_callback)
    self.tfshow = tfshow

  def tf_callback(tf_stampeds):
    for tf_stamped in tf_stampeds.transforms():
      frame_id = tf_stamped.header().frame_id()
      child_frame_id = tf_stamped.child_frame_id()

      self.tfshow.add_tf(frame_id, child_frame_id)
