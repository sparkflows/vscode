# Sensor Nodes

## AWS
- **S3 Sensor** `06-Sensor/s3Sensor.json` — This node supports s3 key Sensor operations.

## EMR
- **EMR Job Flow Sensor** `06-Sensor/emrJobFlowSensor.json` — This node will periodically check if the state of the EMR JobFlow (Cluster) reaches any of the target states.
- **EMR Step Sensor** `06-Sensor/emrStepSensor.json` — This node will periodically check if the last added step in EMR is completed or skipped or terminated.

## EMR Serverless
- **EMR Serverless Application Sensor** `06-Sensor/EmrServerlessApplicationSensor.json` — This node will periodically check if the state of the EMR Serverless application reaches any of the target states.
- **EMR Serverless Job Sensor** `06-Sensor/EmrServerlessJobSensor.json` — This node will periodically check if the state of the EMR Serverless Job run reaches any of the target states.
