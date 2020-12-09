# Comandos

### Crie um Container Registry (a menos que já exista)

```bash
docker run -d -p 5000:5000 --restart always --name kind-registry registry:2
```

### Criar um Cluster com o Registry Local habilitado no ContainerD

```bash
kind create cluster --name local --config ./k8s/cluster/kind-config.yaml
```

### Confira as redes e containers existentes

```bash
docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Ports}}\t{{.Status}}"
docker network ls
```

### Verificar a rede atual do Registry

```bash
docker inspect --format='{{json .NetworkSettings.Networks}}' kind-registry
```

### Connect o Registry à rede do Cluster (a rede pode já estar conectada)

```bash
docker network connect kind kind-registry
docker inspect --format='{{json .NetworkSettings.Networks}}' kind-registry
```

### Configura o Local Registry no k8s

```bash
kubectl apply -f ./k8s/cluster/kind-registry-hosting.yaml
```

### Build da imagem

```bash
docker build -t localhost:5000/kr:0.1.0-dev .
```

### Push da imagem para o Local Registry

```bash
docker push localhost:5000/kr:0.1.0-dev
```

### Aplica receitas do k8s para a aplicação

```bash
kubectl apply -f ./k8s/app/configmap.yaml
kubectl apply -f ./k8s/app/deployment.yaml
kubectl apply -f ./k8s/app/service.yaml
```
