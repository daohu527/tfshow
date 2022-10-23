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

import argparse
import logging
import sys

from google.protobuf import text_format

from cyber_record.record import Record
from tfshow.tfshow import TfShow

def add_tf(tfshow, tf_stampeds):
  for tf_stamped in tf_stampeds.transforms:
    frame_id = tf_stamped.header.frame_id
    child_frame_id = tf_stamped.child_frame_id
    tfshow.add_tf(frame_id, child_frame_id,
        text_format.MessageToString(tf_stamped.transform))

def read_tf(file_name, tfshow):
  record = Record(file_name)
  tf_counts = {'/tf':0, '/tf_static':0}
  for topic, message, t in record.read_messages(['/tf','/tf_static']):
    logging.debug("{}, {}, {}".format(topic, type(message), t))
    # Because most of them are duplicate messages, only 10 are read
    if tf_counts['/tf_static'] >= 1 and tf_counts['/tf'] >= 10:
      break
    add_tf(tfshow, message)
    tf_counts[topic] += 1


def main(args=sys.argv):
  parser = argparse.ArgumentParser(
    description="cyber tf visualizer.", prog="main.py")

  parser.add_argument(
    "-f", "--file", action="store", type=str, required=True,
    nargs='?', const="", help="cyber record file")

  parser.add_argument(
    "-m", "--mode", action="store", type=str, required=False,
    nargs='?', const="", help="display mode")


  args = parser.parse_args(args[1:])

  # 1. read tf from record file
  tfshow = TfShow()
  read_tf(args.file, tfshow)

  # 2. show tf
  if args.mode == 'p':
    tfshow.print()
  elif args.mode == 'v':
    tfshow.view()
  elif args.mode == 's':
    tfshow.save("tf.svg")
  else:
    tfshow.view()
