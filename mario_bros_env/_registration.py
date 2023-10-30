"""Registration code of Gym environments in this package."""
import gymnasium as gym


def _register_mario_env(id, is_random=False, **kwargs):
    """
    Register a Super Mario Bros. (1/2) environment with Farama Gymnasium.

    Args:
        id (str): id for the env to register
        is_random (bool): whether to use the random levels environment
        kwargs (dict): keyword arguments for the SuperMarioBrosEnv initializer

    Returns:
        None

    """
   
    # set the entry point to the standard Super Mario Bros. environment
    entry_point = 'mario_bros_env:SuperMarioBrosEnv'
    # register the environment
    gym.envs.registration.register(
        id=id,
        entry_point=entry_point,
        max_episode_steps=9999999,
        reward_threshold=9999999,
        kwargs=kwargs,
        nondeterministic=True,
    )


# Super Mario Bros.
_register_mario_env('SuperMarioBros-v0')

def _register_mario_stage_env(id, **kwargs):
    """
    Register a Super Mario Bros. stage environment with Farama Gymnasium.

    Args:
        id (str): id for the env to register
        kwargs (dict): keyword arguments for the SuperMarioBrosEnv initializer

    Returns:
        None

    """
    # register the environment
    gym.envs.registration.register(
        id=id,
        entry_point='mario_bros_env:SuperMarioBrosEnv',
        max_episode_steps=9999999,
        reward_threshold=9999999,
        kwargs=kwargs,
        nondeterministic=True,
    )


# a template for making individual stage environments
_ID_TEMPLATE = 'SuperMarioBros-{}-{}-v0'



# iterate over all the rom modes, worlds (1-8), and stages (1-4)
for world in range(1, 9):
    for stage in range(1, 5):
        # create the target
        target = (world, stage)
        # setup the frame-skipping environment
        env_id = _ID_TEMPLATE.format(world, stage)
        _register_mario_stage_env(env_id, target=target)


# create an alias to gym.make for ease of access
make = gym.make


# define the outward facing API of this module (none, gym provides the API)
__all__ = [make.__name__]
