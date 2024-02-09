ARG GLUE_VERSION="4.0.0"

FROM amazon/aws-glue-libs:glue_libs_${GLUE_VERSION}_image_01

ARG USER=glue_user
USER $USER

ARG DELTA_LAKE_VERSION="2.1.0"
RUN pip3 install delta-spark==$DELTA_LAKE_VERSION

RUN curl -o ${SPARK_HOME}/jars/spark-xml_2.12-0.17.0.jar https://repo1.maven.org/maven2/com/databricks/spark-xml_2.12/0.17.0/spark-xml_2.12-0.17.0.jar