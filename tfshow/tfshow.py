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


import graphviz
import logging

class TfShow(object):
  def __init__(self):
    self.dot = graphviz.Digraph('tf graph', strict=True)

  def add_tf(self, node_a, node_b, edge_label=None):
    self.dot.node(node_a)
    self.dot.node(node_b)
    self.dot.edge(node_a, node_b, label=edge_label)

  def print(self):
    print(self.dot.source)

  def view(self):
    # todo(zero): add doctest_mark_exe will cause not found error!!!
    # doctest_mark_exe()
    self.dot.view()

  def save(self, file_name):
    # doctest_mark_exe()
    self.dot.render(file_name, view=True)
