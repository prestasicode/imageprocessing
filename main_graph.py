# issue define pipeline_config

def main(_):
      pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
  with tf.gfile.GFile(FLAGS.pipeline_config_path, 'r') as f:
    text_format.Merge(f.read(), pipeline_config)
  text_format.Merge(FLAGS.config_override, pipeline_config)
  if FLAGS.input_shape:
    input_shape = [
        int(dim) if dim != '-1' else None
        for dim in FLAGS.input_shape.split(',')
    ]
#pipeline_config call variables
  else:
    input_shape = None
  exporter.export_inference_graph(FLAGS.input_type, pipeline_config,
                                  FLAGS.trained_checkpoint_prefix,
                                  FLAGS.output_directory, input_shape,
                                  FLAGS.write_inference_graph)


if __name__ == '__main__':
  tf.app.run()
