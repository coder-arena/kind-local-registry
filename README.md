# Kind Local Registry

> Arquivos utilizados no vídeo [**Usando container Registry local com Kind**](https://youtu.be/NEo36iGB6Mw)

Projeto criado para demonstração do uso de um Registry local no Kubernetes com Kind.

[**O VÍDEO COMPLETO ESTÁ DISPONÍVEL AQUI!**](https://youtu.be/NEo36iGB6Mw)

Um registro de contêiner é um repositório, ou coleção de repositórios, usado para armazenar imagens de contêiner. Existem dois tipos de registro de contêiner: **público** e **privado**. 

Atualmente existem diversas soluções para execução de cluster kubernetes localmente, como o MicroK8S, K3d, Minikube e o Kind.

E todas as soluções já suportam o uso de um registry local, no entanto para que seja possível recuperar uma imagem que só existe no seu computador você precisará de um servidor de registro de imagens local, assim o Hub do docker, o AWS ECR, só que na sua máquina.

## Requisitos

Para que sua experiência com a reprodução dos passos executados no vídeo seja o mais simples possível, você precisará ter:

- Um editor, eu utilizo o [VSCode](https://code.visualstudio.com/) (para visualizar e testar alterações);
- [Docker](https://www.docker.com/) (utilizado para subir o cluster [Kubernetes](http://kubernetes.io/) local);
- [Kind](https://kind.sigs.k8s.io/) (para criação de cluster local);
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) (para interagir com o cluster);

## Comandos

Todos os comandos usados estão presentes no arquivo [`COMMANDS.md`](COMMANDS.md).

Siga com atenção :wink:

## Seu apoio

Dê uma ⭐️ se esse projeto ajudou você!

Aproveite e [inscreva-se no canal](https://youtube.com/channel/UC9ljALQ1KcfatYfoo_MqSgQ?sub_confirmation=1) para ser notificado sempre que um vídeo novo sair.

Quer fazer parte da Lista VIP para receber conteúdos exclusivos? [Cadastre-se aqui.](https://news.coderarena.com.br/)

## Desenvolvimento

Todas as operações do serviço podem ser realizadas pelo `docker-compose`. Abaixo estão as ações possíveis e uma pequena explicação de seu funcionamento.

### API

No seu terminal, na pasta do projeto basta executar o comando abaixo para aplicação iniciar localmente.

```bash
docker-compose up app
```

### Lint

A verificação de estilo de código é feita através do comando abaixo:

```bash
docker-compose up lint
```

Esse serviço irá aplicar verificações com [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort), [`mypy`](https://github.com/python/mypy), [`pycodestyle`](https://github.com/PyCQA/pycodestyle) e [`flake8`](https://github.com/PyCQA/flake8).

## Referências

- https://kind.sigs.k8s.io/docs/user/local-registry/
- https://hub.docker.com/_/registry
- https://github.com/kubernetes/enhancements/tree/master/keps/sig-cluster-lifecycle/generic/1755-communicating-a-local-registry#design-details
- https://docs.docker.com/engine/reference/commandline/network_connect/
- https://docs.docker.com/engine/reference/run/
